import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("notebook", "data", "online_retail.csv")
    purchase_data_path: str = os.path.join("artifacts", "purchase_view.csv")
    return_data_path: str = os.path.join("artifacts", "return_view.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting Data Ingestion component.")
        try:
            df_raw = pd.read_csv(self.ingestion_config.raw_data_path, encoding='latin1')
            logging.info(f"Loaded raw dataset with {len(df_raw):,} records.")

            # Standardize column strings
            df_raw['InvoiceNo'] = df_raw['InvoiceNo'].astype(str).str.strip()
            df_raw['StockCode'] = df_raw['StockCode'].astype(str).str.strip()
            df_raw['Description'] = df_raw['Description'].astype(str).str.strip()
            df_raw['InvoiceDate'] = pd.to_datetime(df_raw['InvoiceDate'])

            admin_codes = ['POST', 'D', 'M', 'BANK CHARGES', 'PADS', 'DOT', 'CRUK']
            df_valid = df_raw[~df_raw['StockCode'].isin(admin_codes)].copy()

            # Separate Purchase View (Positive sales with known CustomerID)
            df_purchase = df_valid[
                (df_valid['CustomerID'].notnull()) &
                (~df_valid['InvoiceNo'].str.startswith('C')) &
                (df_valid['Quantity'] > 0) &
                (df_valid['UnitPrice'] > 0)
            ].copy()
            df_purchase['CustomerID'] = df_purchase['CustomerID'].astype(int).astype(str)
            df_purchase['LineValue'] = df_purchase['Quantity'] * df_purchase['UnitPrice']

            # Separate Return View (Cancellations and negative quantities)
            df_return = df_valid[
                (df_valid['CustomerID'].notnull()) &
                ((df_valid['InvoiceNo'].str.startswith('C')) | (df_valid['Quantity'] < 0))
            ].copy()
            df_return['CustomerID'] = df_return['CustomerID'].astype(int).astype(str)
            df_return['ReturnValue'] = df_return['Quantity'].abs() * df_return['UnitPrice']

            os.makedirs(os.path.dirname(self.ingestion_config.purchase_data_path), exist_ok=True)
            df_purchase.to_csv(self.ingestion_config.purchase_data_path, index=False)
            df_return.to_csv(self.ingestion_config.return_data_path, index=False)

            logging.info(f"Data Ingestion completed: {len(df_purchase):,} purchase lines, {len(df_return):,} return lines saved to artifacts.")
            return self.ingestion_config.purchase_data_path, self.ingestion_config.return_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.initiate_data_ingestion()