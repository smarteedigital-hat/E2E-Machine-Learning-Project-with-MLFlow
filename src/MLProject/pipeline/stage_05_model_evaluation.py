from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_evaluation import ModelEvaluation
from MLProject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        logger.info(f"<<<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()
        logger.info(f"<<<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")

if __name__ == "__main__":
    try:
        logger.info(f"<<<<<<<< {STAGE_NAME} started >>>>>>>>>>>>>>>>")
        pipeline = ModelEvaluationPipeline()
        pipeline.run()
        logger.info(f"<<<<<<<< {STAGE_NAME} completed >>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in model evaluation pipeline: {e}")