import os
import sys
import numpy as np
from flask import Flask, request, jsonify
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.GetClientIP import GetClientIP
from service.GetRecommendationsService import GetRecommendationsService

from functions.CalculateSimilarity import CalculateSimilarity
from functions.LoadData import LoadData
from functions.SaveData import SaveData
from functions.PreprocessData import PreprocessData

app = Flask(__name__)

class RecommendationsController:

    app.config['UPLOAD_FOLDER'] = 'uploads/user_files'

    @app.route('/upload', methods=['POST'])
    def upload_file():
        # Verifica se a requisição contém a parte 'file'
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        
        # Verifica se o nome do arquivo está vazio
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        file_extension = file.filename.split('.')[-1]
        
        if file_extension in ['tsv', 'csv', 'xlsx', 'xls', 'json']:
            # Usa o endereço IP do cliente como user_id
            user_id = request.remote_addr
            
            # Define o caminho da pasta do usuário
            user_folder = os.path.join(app.config['UPLOAD_FOLDER'], user_id)
            
            # Cria a pasta do usuário, se não existir
            os.makedirs(user_folder, exist_ok=True)
            
            # Define o caminho completo do arquivo
            filepath = os.path.join(user_folder, file.filename)
            
            # Salva o arquivo no caminho especificado
            file.save(filepath)
            
            # Carrega os dados do arquivo para um DataFrame
            movies = LoadData.load_data(filepath, file_extension)

            movies = PreprocessData.preprocess_data(movies)
            SaveData.save_data(movies, filepath, file_extension)
            
            # Calcula a similaridade dos filmes
            cosine_sim = CalculateSimilarity.calculate_similarity(movies)
            
            # Salva a matriz de similaridade em um arquivo .npy
            similarity_folder = os.path.join('data', 'similarity', user_id)
            os.makedirs(similarity_folder, exist_ok=True)
            np.save(os.path.join(similarity_folder, f'{file.filename}_cosine_sim.npy'), cosine_sim)
            
            return jsonify({'message': 'File uploaded and processed successfully'}), 200
        else:
            return jsonify({'error': 'Invalid file format. Please upload a .tsv, .csv, .xlsx, .xls or .json file.'}), 400


    @app.route('/recommend', methods=['GET'])
    def recommend_route():
        data = request.get_json()

        id = data.get('id')
        quantity = data.get('quantity')
        file_name = data.get('file_name')
        user_id = GetClientIP.get_client_ip(request)
        if user_id is None:
            return jsonify({'error': 'Unable to get user IP'}), 400
        
        recommendations = GetRecommendationsService.get_recommendations(id, quantity, user_id, file_name)
        if 'error' in recommendations:
            return jsonify(recommendations), 400
        return jsonify({'recommendations': recommendations}), 200

if __name__ == '__main__':
    app.run(debug=True)
