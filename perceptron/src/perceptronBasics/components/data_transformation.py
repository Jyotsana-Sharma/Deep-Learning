from perceptronBasics.config.configuration import DataTransformationConfig
import pandas as pd 


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def handle_missing_values(self, row):
        row.fillna(row.mean(), inplace=True)
        return row

    def handle_duplicate_values(self, row):
        row.drop_duplicates(inplace=True)
        return row

    def convert(self):
        dataset = pd.read_csv(self.config.data_path)
        transformed_dataset = dataset.apply(self.handle_missing_values, axis=1)
        transformed_dataset = dataset.apply(self.handle_duplicate_values, axis=0)
        transformed_dataset.to_csv(os.path.join(self.config.root_dir,"transformed_dataset"))