import os
import sys
import pandas as pd
import numpy as np
import datetime as dt
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

@dataclass
class SegmentationConfig:
    preprocessor_path: str = os.path.join("artifacts", "preprocessor.pkl")
    kmeans_model_path: str = os.path.join("artifacts", "kmeans_model.pkl")
    segmented_data_path: str = os.path.join("artifacts", "customer_segmented_data.csv")

class CustomerSegmentation:
    def __init__(self):
        self.config = SegmentationConfig()

    def initiate_segmentation(self, purchase_data_path: str):
        logging.info("Starting Customer Segmentation component.")
        try:
            df_purchases = pd.read_csv(purchase_data_path)
            df_purchases['InvoiceDate'] = pd.to_datetime(df_purchases['InvoiceDate'])

            snapshot_date = df_purchases['InvoiceDate'].max() + dt.timedelta(days=1)

            # Aggregate to Customer Level
            cust_df = df_purchases.groupby('CustomerID').agg(
                Recency=('InvoiceDate', lambda x: (snapshot_date - x.max()).days),
                Frequency=('InvoiceNo', 'nunique'),
                Monetary=('LineValue', 'sum'),
                DistinctSKUs=('StockCode', 'nunique')
            ).reset_index()
            cust_df['AvgOrderValue'] = (cust_df['Monetary'] / cust_df['Frequency']).round(2)

            # RFM Scoring 1 to 5
            cust_df['R_Score'] = pd.qcut(cust_df['Recency'], q=5, labels=[5, 4, 3, 2, 1]).astype(int)
            cust_df['F_Score'] = pd.qcut(cust_df['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
            cust_df['M_Score'] = pd.qcut(cust_df['Monetary'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)

            # 7-Tier Hierarchical Rule Engine
            def assign_segment(row):
                r, f, m, freq = row['R_Score'], row['F_Score'], row['M_Score'], row['Frequency']
                if freq == 1 and r >= 4:
                    return 'New Customers'
                if r >= 4 and f >= 4 and m >= 4:
                    return 'Champions'
                if r >= 3 and f >= 4:
                    return 'Loyal Customers'
                if r <= 2 and (f >= 4 or m >= 4):
                    return 'At Risk Valuable'
                if r >= 4:
                    return 'Promising Customers'
                if r <= 2:
                    return 'Hibernating'
                return 'Developing Customers'

            cust_df['Segment'] = cust_df.apply(assign_segment, axis=1)

            # K-Means Clustering on Scaled Log(RFM)
            rfm_log = np.log1p(cust_df[['Recency', 'Frequency', 'Monetary']])
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(rfm_log)

            kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
            cust_df['Cluster_ID'] = kmeans.fit_predict(scaled_features)

            # 2D PCA Projection
            pca = PCA(n_components=2, random_state=42)
            coords = pca.fit_transform(scaled_features)
            cust_df['PCA1'] = coords[:, 0]
            cust_df['PCA2'] = coords[:, 1]

            # Save models and artifacts
            save_object(self.config.preprocessor_path, scaler)
            save_object(self.config.kmeans_model_path, kmeans)
            cust_df.to_csv(self.config.segmented_data_path, index=False)

            logging.info(f"Segmentation completed: {len(cust_df):,} customers segmented and artifacts saved.")
            return self.config.segmented_data_path

        except Exception as e:
            raise CustomException(e, sys)