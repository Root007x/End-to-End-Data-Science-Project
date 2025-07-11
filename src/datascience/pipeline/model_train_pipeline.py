from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger



STAGE_NAME = "MODEL TRAIN"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_train(self):
        config = ConfigurationManager()
        model_train_config = config.get_model_trainer_config()
        model_train = ModelTrainer(config=model_train_config)
        model_train.train()

        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_train()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e