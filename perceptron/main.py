from perceptronBasics.logging import logger
from perceptronBasics.pipeline.stage_01_data_ingestion_pipleline import DataIngestionPipeline



STAGE_NAME = "Data Ingestion Stage"


logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
data_ingestion = DataIngestionPipeline()
data_ingestion.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


