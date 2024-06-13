import pandas as pd

class PreprocessData:

    @staticmethod
    def preprocessData(df: pd.DataFrame, id_column_name: str, title_column_name: str) -> pd.DataFrame:

        for column in df.columns:
            df[column] = df[column].astype(str).fillna('')

        columns_to_combine = [col for col in df.columns if col != id_column_name]
        
        df['combined_features'] = df[columns_to_combine].apply(lambda row: ' '.join(row.values), axis=1)

        columns_order = [id_column_name, title_column_name] + [col for col in df.columns if col not in [id_column_name, title_column_name, 'combined_features']] + ['combined_features']
        df = df[columns_order]

        return df

