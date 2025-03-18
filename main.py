from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_transformation import DataTransformation
import sys
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        data_validataion_config = DataValidationConfig(training_pipeline_config)
        logging.info('initiated data ingestion')
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation=DataValidation(dataingestionartifact, data_validataion_config)
        logging.info('Initiate the data validation')
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('data validation completed')
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        logging.info('Data transformation started')
        data_transformation=DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info('Data transformation completed')
        print(data_transformation_artifact)

        logging.info("Model trainer started")
        model_trainer_config=ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info('Model trainer artifact created')
        


    except Exception as e:
        raise NetworkSecurityException(e,sys)