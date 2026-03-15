import os
from MLProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from MLProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: Should be add different data transformation techniques such as Scaler, PCA, and all
    # Should be performed all kinds of EDA in ML cycle here before passing this data to the model

    # It is gonna be only adding train_test_splitting cz this data is already cleaned

    def train_test_splitting(self):
        data = pd.read_csv(self.config.local_data_file)
        
        # Split the data into training and test sets. (0.75, 0.25) split
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into train and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)