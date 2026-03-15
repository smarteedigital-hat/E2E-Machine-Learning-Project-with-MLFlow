from MLProject.config.configuration import ConfigurationManager
from MLProject.components.data_transformation import DataTransformation
from MLProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(f"<<<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")

            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                logger.info("Data validation passed")

                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
                logger.info(f"<<<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
            else:
                logger.error("Data validation failed")
                raise Exception("Data validation failed")
        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e

    if __name__ == "__main__":
        try:
            logger.info(f"<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
            data_transformation_pipeline = DataTransformationPipeline()
            data_transformation_pipeline.run()
            logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e