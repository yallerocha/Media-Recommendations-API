import os
from typing import Union

class RecommendationsValidator:

    @staticmethod
    def file_nameValidate(user_id: str, file_name: str) -> Union[None, dict]:
        if file_name is None:
            return {"error": "File name is required"}
        if len(file_name.strip()) == 0:
            return {"error": "File name cannot be empty"}

        user_folder = os.path.join('uploads/user_files', user_id)
        file_path = os.path.join(user_folder, file_name)
        
        if not os.path.exists(file_path):
            return {"error": "File does not exist"}
        
        return None

    @staticmethod
    def idValidate(id: str) -> Union[None, dict]:
        if id is None:
            return {"error": "id is required"}
        if len(id.strip()) == 0:
            return {"error": "id cannot be empty"}
        
        return None
        
    @staticmethod
    def quantityValidate(quantity: int, file_size: int) -> Union[None, dict]:
        if quantity is None:
            return {"error": "Quantity is required"}
        if not isinstance(quantity, int):
            return {"error": "Quantity must be an integer"}
        if quantity <= 0:
            return {"error": "Quantity must be greater than 0"}
        if quantity > file_size - 1:
            return {"error": "Quantity must be less than the number of rows in the file"}

        return None