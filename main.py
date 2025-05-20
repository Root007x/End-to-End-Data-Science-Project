from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipleline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_train_pipeline import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipleline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Train Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.initiate_model_train()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_eval = ModelEvaluationPipeline()
    model_eval.initiate_model_eval()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


