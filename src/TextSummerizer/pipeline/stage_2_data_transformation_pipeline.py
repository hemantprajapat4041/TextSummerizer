from src.TextSummerizer.config.configuration import ConfigurationManager
from src.TextSummerizer.components.data_transformation import DataTransformation
from src.TextSummerizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
         pass
    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(data_transformation_config)
        data_transformation.convert()