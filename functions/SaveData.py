import pandas as pd

class SaveData:

    @staticmethod
    def saveData(df: pd.DataFrame, file_path, file_extension):
        if file_extension == 'tsv':
            df.to_csv(file_path, sep='\t', index=False)
        elif file_extension == 'csv':
            df.to_csv(file_path, index=False)
        elif file_extension == 'xlsx':
            df.to_excel(file_path, index=False)
        elif file_extension == 'xls':
            df.to_excel(file_path, index=False)
        elif file_extension == 'json':
            df.to_json(file_path, orient='records', lines=True)