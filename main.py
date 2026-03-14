from MLProject import logger
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline

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