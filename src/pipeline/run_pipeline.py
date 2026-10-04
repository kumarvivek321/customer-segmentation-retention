import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.customer_segmentation import CustomerSegmentation
from src.components.retention_analyzer import RetentionAnalyzer

def execute_pipeline():
    logging.info(">>> INITIATING FULL END-TO-END RETAIL ANALYTICS PIPELINE <<<")
    try:
        # Step 1: Ingestion
        ingestion = DataIngestion()
        purchase_path, return_path = ingestion.initiate_data_ingestion()
        print(f"[+] Data Ingestion Complete -> {purchase_path}")

        # Step 2: Segmentation
        segmentation = CustomerSegmentation()
        segmented_path = segmentation.initiate_segmentation(purchase_path)
        print(f"[+] Customer Segmentation Complete -> {segmented_path}")

        # Step 3: Retention Analysis
        retention = RetentionAnalyzer()
        watchlist_path = retention.initiate_retention_analysis(segmented_path)
        print(f"[+] Retention Watchlist Complete -> {watchlist_path}")

        print("\n[SUCCESS] COMPLETE END-TO-END PIPELINE EXECUTED SUCCESSFULLY!")
        logging.info(">>> PIPELINE EXECUTION FINISHED SUCCESSFULLY <<<")

    except Exception as e:
        logging.error("Pipeline failed with exception.")
        raise CustomException(e, sys)

if __name__ == "__main__":
    execute_pipeline()