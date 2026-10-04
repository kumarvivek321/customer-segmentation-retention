import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

@dataclass
class RetentionConfig:
    watchlist_path: str = os.path.join("artifacts", "retention_watchlist.csv")

class RetentionAnalyzer:
    def __init__(self):
        self.config = RetentionConfig()

    def initiate_retention_analysis(self, segmented_data_path: str):
        logging.info("Starting Retention Analysis component.")
        try:
            cust_df = pd.read_csv(segmented_data_path)
            
            # High-Value At-Risk Watchlist (Recency > 90 days and High Value)
            inactivity_threshold = 90
            at_risk = cust_df[
                (cust_df['Recency'] > inactivity_threshold) &
                ((cust_df['Segment'].isin(['Champions', 'Loyal Customers', 'At Risk Valuable'])) | (cust_df['Monetary'] >= 1000))
            ].sort_values(by='Monetary', ascending=False).copy()

            at_risk['RetentionRiskCategory'] = 'High Value At-Risk (Urgent Intervention)'
            at_risk.to_csv(self.config.watchlist_path, index=False)

            logging.info(f"Retention Analysis completed: {len(at_risk):,} high-value at-risk accounts exported to {self.config.watchlist_path}.")
            return self.config.watchlist_path

        except Exception as e:
            raise CustomException(e, sys)