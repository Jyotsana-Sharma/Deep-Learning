from perceptronBasics.config.configuration import ConfigurationManager
from perceptronBasics.entity import DataIngestionConfig
from perceptronBasics.components.data_validation import DataValidation
from perceptronBasics.logging import logger





class DataValidationPipeline:
    try: 
        config = ConfigurationManager()
        data_valid_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_valid_config)
        data_validation.validate_all_files_exist()
    except Exception as e : 
        logger.error(f'Validation Error : {e}')
