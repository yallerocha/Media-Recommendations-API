import pandas as pd

class PreprocessData:

    @staticmethod
    def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:

        # Convert all columns to string and fill NaN with empty string
        for column in df.columns:
            df[column] = df[column].astype(str).fillna('')

        # Exclude the ID column from the combined features
        columns_to_combine = [col for col in df.columns if col != 'tconst']
        
        # Create the combined_features column
        df['combined_features'] = df[columns_to_combine].apply(lambda row: ' '.join(row.values), axis=1)

        return df

