from MLProject import logger
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from MLProject.pipeline.stage_02_data_validation import DataValidationPipeline
from MLProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from MLProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

    
    STAGE_NAME = "Data Validation stage"
    try:
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>")
        pipeline = DataValidationPipeline()
        pipeline.run()
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>")
        pipeline = DataTransformationPipeline()
        pipeline.run()
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

    STAGE_NAME = "Model Training stage"
    try:
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>")
        pipeline = ModelTrainerPipeline()
        pipeline.run()
        logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e