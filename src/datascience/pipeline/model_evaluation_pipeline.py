from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger



STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_eval(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.log_into_mlflow()

        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_eval()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e