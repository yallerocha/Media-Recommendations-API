from typing import Union

import pandas as pd

class UploadFileValidator:

    @staticmethod
    def idColumnNameValidate(id_column: str, movies: pd.DataFrame) -> Union[None, dict]:
        if id_column is None:
            return {"error": "idColumn parameter is required"}
        if len(id_column.strip()) == 0:
            return {"error": "idColumn parameter cannot be empty"}
        if id_column not in movies.columns:
            return {"error": f"Column '{id_column}' does not exist"}
        if movies[id_column].isnull().any():
            return {"error": f"Column '{id_column}' contains missing values"}
        if not movies[id_column].is_unique:
            return {"error": f"Column '{id_column}' contains duplicate values"}

        return None
    
    @staticmethod
    def titleColumnNameValidate(title_column: str, movies: pd.DataFrame) -> Union[None, dict]:
        if title_column is None:
            return {"error": "titleColumn parameter is required"}
        if len(title_column.strip()) == 0:
            return {"error": "titleColumn parameter cannot be empty"}
        if title_column not in movies.columns:
            return {"error": f"Column '{title_column}' does not exist"}

        return None
    
    @staticmethod
    def fileExtensionValidate(file_extension: str) -> Union[None, dict]:
        if file_extension not in ['tsv', 'csv', 'xlsx', 'xls', 'json']:
            return {"error": 'Invalid file format. Please upload a .tsv, .csv, .xlsx, .xls or .json file.'}

        return None