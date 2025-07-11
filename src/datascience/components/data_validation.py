from src.datascience import logger
from src.datascience.entity.config_entity import (DataValidationConfig)
import pandas as pd




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            all_dtypes = [str(dtype) for dtype in data.dtypes]
            all_schema_key = self.config.all_schema.keys()
            all_schema_value = self.config.all_schema.values()

            for col,type in zip(all_columns, all_dtypes):
                if col not in all_schema_key and type not in all_schema_value:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation Status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e