import pandas as pd

class PreprocessData:

    @staticmethod
    def preprocess_data(df: pd.DataFrame, idColumn: str, titleColumn: str) -> pd.DataFrame:

        for column in df.columns:
            df[column] = df[column].astype(str).fillna('')

        columns_to_combine = [col for col in df.columns if col != idColumn]
        
        df['combined_features'] = df[columns_to_combine].apply(lambda row: ' '.join(row.values), axis=1)

        columns_order = [idColumn, titleColumn] + [col for col in df.columns if col not in [idColumn, titleColumn, 'combined_features']] + ['combined_features']
        df = df[columns_order]

        return df

