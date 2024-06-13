import os

class ListFilesService:

    def listFiles(user_id: str):
        user_folder = os.path.join("API/uploads/user_files", user_id)
        
        if not os.path.exists(user_folder):
            return {'error': 'No files found for this user'}
        
        files = os.listdir(user_folder)
        if not files:
            return {'message': 'No files found for this user'}
        
        return {'files': [file for file in files]}