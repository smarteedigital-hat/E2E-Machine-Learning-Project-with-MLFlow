from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_ingestion import DataIngestion
from MLProject import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def run(self):
        try:
            logger.info(f"<<<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info(f"<<<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME}: {e}")
            raise e

if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info(f"<<<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e