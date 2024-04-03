from perceptronBasics.logging import logger
from perceptronBasics.pipeline.stage_01_data_ingestion_pipleline import DataIngestionPipeline
from perceptronBasics.pipeline.stage_02_data_validation_pipeline import DataValidationPipeline



STAGE_NAME = "Data Ingestion Stage"


logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
data_ingestion = DataIngestionPipeline()
data_ingestion.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

STAGE_NAME = "Data Validation  Stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
data_validation = DataValidationPipeline()
data_validation.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


