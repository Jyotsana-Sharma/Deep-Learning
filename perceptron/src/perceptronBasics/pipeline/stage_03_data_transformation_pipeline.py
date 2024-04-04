from perceptronBasics.config.configuration import ConfigurationManager
from perceptronBasics.entity import DataIngestionConfig, DataTransformationConfig
from perceptronBasics.components.data_validation import DataValidation
from perceptronBasics.components.data_transformation import DataTransformation,DataTransformationConfig
from perceptronBasics.logging import logger




class DataTransformationPipeline:
    try:
        config = ConfigurationManager() 
        data_transformed = config.get_data_transformation_config()
        data_transformation_obj = DataTransformation(config= data_transformed)
        data_transformation_obj.convert()
    except Exception as e: 
        logger.error(f'Exception as : {e}')  

