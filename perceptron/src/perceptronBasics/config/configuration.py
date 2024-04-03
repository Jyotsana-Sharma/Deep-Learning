from perceptronBasics.constants import *
from perceptronBasics.utils.common import read_yaml, create_directories
from perceptronBasics.entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self,config_file_path = CONFIG_FILE_PATH , param_file_path = PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        # self.param_file = read_yaml(param_file_path)

        create_directories([self.config.artifacts_root])
    

    def get_data_ingestion_config(self)->DataIngestionConfig: 
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(root_dir=config.root_dir, source_URL=config.source_URL, local_data_file=config.local_data_file)

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(root_dir = config.root_dir, STATUS_FILE= config.STATUS_FILE, ALL_REQUIRED_FILES= config.ALL_REQUIRED_FILES)

        return data_validation_config