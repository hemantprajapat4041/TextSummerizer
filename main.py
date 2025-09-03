from src.TextSummerizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
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


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"stage{STAGE_NAME} INITIATED")
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"stage{STAGE_NAME} COMPLETED")

except Exception as e:
    logger.exception(e)
    raise(e)