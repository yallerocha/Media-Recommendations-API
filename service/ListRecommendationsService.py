from typing import List, Union
import numpy as np

from functions.LoadData import LoadData
from validator.RecommendationsValidator import RecommendationsValidator  

class ListRecommendationsService:

    @staticmethod 
    def listRecommendations(movie_id: str, quantity: int, user_id: str, file_name: str) -> Union[List[dict], dict]:

        result = RecommendationsValidator.fileValidate(user_id, file_name)
        if result is not None:
            return result
        result = RecommendationsValidator.idValidate(movie_id)  
        if result is not None:
            return result
        
        file_size = LoadData.loadData(f'uploads/user_files/{user_id}/{file_name}', file_name.split('.')[-1]).shape[0]

        result = RecommendationsValidator.quantityValidate(quantity, file_size)
        if result is not None:
            return result

        cosine_sim = np.load(f'data/similarity/{user_id}/{file_name}_cosine_sim.npy')

        media_table = LoadData.loadData(f'uploads/user_files/{user_id}/{file_name}', file_name.split('.')[-1])

        id_column_name = media_table.columns[0]
        title_column_name = media_table.columns[1]

        try:
            idx = media_table[media_table[id_column_name] == movie_id].index[0]
        except IndexError:
            return {"error": f"Movie with ID {movie_id} not found"}

        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:quantity + 1]
        movie_indices = [i[0] for i in sim_scores]

        recommendations = [
            {id_column_name: media_table.at[i, id_column_name], title_column_name: media_table.at[i, title_column_name]}
            for i in movie_indices
        ]

        return recommendations

