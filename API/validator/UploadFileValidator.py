from typing import Union

import pandas as pd

class UploadFileValidator:

    @staticmethod
    def idColumnNameValidate(id_column_name: str, media_table: pd.DataFrame) -> Union[None, dict]:
        if id_column_name is None:
            return {"error": "id_column_name parameter is required"}
        if len(id_column_name.strip()) == 0:
            return {"error": "id_column_name parameter cannot be empty"}
        if id_column_name not in media_table.columns:
            return {"error": f"Column '{id_column_name}' does not exist"}
        if media_table[id_column_name].isnull().any():
            return {"error": f"Column '{id_column_name}' contains missing values"}
        if not media_table[id_column_name].is_unique:
            return {"error": f"Column '{id_column_name}' contains duplicate values"}

        return None
    
    @staticmethod
    def titleColumnNameValidate(title_column: str, media_table: pd.DataFrame) -> Union[None, dict]:
        if title_column is None:
            return {"error": "title_column_name parameter is required"}
        if len(title_column.strip()) == 0:
            return {"error": "title_column_name parameter cannot be empty"}
        if title_column not in media_table.columns:
            return {"error": f"Column '{title_column}' does not exist"}

        return None
    
    @staticmethod
    def fileExtensionValidate(file_extension: str) -> Union[None, dict]:
        if file_extension not in ['tsv', 'csv', 'xlsx', 'xls', 'json']:
            return {"error": 'Invalid file format. Please upload a .tsv, .csv, .xlsx, .xls or .json file.'}

        return None