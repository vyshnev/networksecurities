from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation


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

    except Exception as e:
        raise NetworkSecurityException(e,sys)