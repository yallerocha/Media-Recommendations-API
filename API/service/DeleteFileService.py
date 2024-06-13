import os

from validator.RecommendationsValidator import RecommendationsValidator

class DeleteFileService:

    @staticmethod
    def deleteFile(user_id: str, file_name: str) -> dict:
        user_folder = os.path.join('api/uploads/user_files', user_id)

        result = RecommendationsValidator.fileValidate(user_id, file_name)
        if result is not None:
            return result

        file_path = os.path.join(user_folder, file_name)
        
        if not os.path.exists(file_path):
            return {"error": "File does not exist"}
        
        try:
            os.remove(file_path)
            os.remove(f'api/data/similarity/{user_id}/{file_name}_cosine_sim.npy')
            return {"message": "File deleted successfully"}
        except Exception as e:
            return {"error": f"Error deleting file: {str(e)}"}
