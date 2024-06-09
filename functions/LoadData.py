import pandas as pd

class LoadData:

    @staticmethod
    def load_data(file_path, file_extension) -> pd.DataFrame:
        if file_extension == 'tsv':
            data = pd.read_csv(file_path, sep='\t')
        elif file_extension == 'csv':
            data = pd.read_csv(file_path)
        elif file_extension == 'xlsx':
            data = pd.read_excel(file_path)
        elif file_extension == 'xls':
            data = pd.read_excel(file_path)
        elif file_extension == 'json':
            data = pd.read_json(file_path)
        
        return data
    
