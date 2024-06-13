import os
import sys
import numpy as np
from flask import Flask, request, jsonify
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.GetClientIP import GetClientIP
from service.GetRecommendationsService import GetRecommendationsService
from service.UploadFileService import UploadFileService

from functions.CalculateSimilarity import CalculateSimilarity
from functions.LoadData import LoadData
from functions.SaveData import SaveData
from functions.PreprocessData import PreprocessData

app = Flask(__name__)

class RecommendationsController:

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return jsonify({'error': 'Missing file parameter'}), 400
        file = request.files['file']
        
        idColumn = request.form.get('idColumn')
        titleColumn = request.form.get('titleColumn')
        user_id = request.remote_addr
        
        result = UploadFileService.upload_file(file, idColumn, titleColumn, user_id)
        if 'error' in result:
            return jsonify(result), 400
        return jsonify(result), 200

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
