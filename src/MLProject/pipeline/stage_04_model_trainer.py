from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_trainer import ModelTrainer
from MLProject import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def run(self):
        try:
            logger.info(f"<<<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")

            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                logger.info("Data validation passed")

                config = ConfigurationManager()
                model_trainer_config = config.get_model_trainer_config()
                model_trainer = ModelTrainer(model_trainer_config)
                model_trainer.train()
                logger.info(f"<<<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
            else:
                logger.error("Data validation failed")
                raise Exception("Data validation failed")
        except Exception as e:
            logger.error(f"Error in model training: {e}")
            raise e

    if __name__ == "__main__":
        try:
            logger.info(f"<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
            model_trainer_pipeline = ModelTrainerPipeline()
            model_trainer_pipeline.run()
            logger.info(f"<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
        except Exception as e:
            logger.error(f"Error in model training: {e}")
            raise e