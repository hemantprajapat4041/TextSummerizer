from src.TextSummerizer.logging import logger
from src.TextSummerizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"stage{STAGE_NAME} INITIATED")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage{STAGE_NAME} COMPLETED")

except Exception as e:
    logger.exception(e)
    raise(e)