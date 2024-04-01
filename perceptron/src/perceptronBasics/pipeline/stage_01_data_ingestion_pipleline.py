from perceptronBasics.config.configuration import ConfigurationManager
from perceptronBasics.entity import DataIngestionConfig
from perceptronBasics.components.data_ingestion import DataIngestion
from perceptronBasics.logging import logger


class DataIngestionPipeline: 
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion.download_file()
        except Exception as e:
            logger.error(e)