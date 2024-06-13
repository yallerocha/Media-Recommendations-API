import os
import numpy as np

from functions.CalculateSimilarity import CalculateSimilarity
from functions.LoadData import LoadData
from functions.PreprocessData import PreprocessData
from functions.SaveData import SaveData

from validator.UploadFileValidator import UploadFileValidator
from werkzeug.datastructures import FileStorage

class UploadFileService:

    @staticmethod
    def uploadFile(file: FileStorage, id_column_name: str, title_column_name: str, user_id: str) -> dict:

        user_folder = os.path.join('uploads/user_files', user_id)

        file_name = file.filename
        if file_name == '':
            return {'error': 'No selected file'}
        file_extension = file_name.split('.')[-1]

        result = UploadFileValidator.fileExtensionValidate(file_extension)
        if result is not None:
            return result
        
        os.makedirs(user_folder, exist_ok=True)
        filepath = os.path.join(user_folder, file_name)
        file.save(filepath)
        
        media_table = LoadData.loadData(filepath, file_extension)

        result = UploadFileValidator.idColumnNameValidate(id_column_name, media_table)
        if result is not None:
            return result
        result = UploadFileValidator.titleColumnNameValidate(title_column_name, media_table)
        if result is not None:
            return result

        media_table = PreprocessData.preprocessData(media_table, id_column_name, title_column_name)
        SaveData.save_data(media_table, filepath, file_extension)
        
        cosine_sim = CalculateSimilarity.calculateSimilarity(media_table)
        
        similarity_folder = os.path.join('data', 'similarity', user_id)
        os.makedirs(similarity_folder, exist_ok=True)
        np.save(os.path.join(similarity_folder, f'{file_name}_cosine_sim.npy'), cosine_sim)

        return {"message": "File uploaded and processed successfully"}