from flask import Flask, request, jsonify

from functions.GetClientIP import GetClientIP
from service.ListRecommendationsService import ListRecommendationsService
from service.UploadFileService import UploadFileService
from service.DeleteFileService import DeleteFileService
from service.ListFilesService import ListFilesService

app = Flask(__name__)

class RecommendationsController:

    @app.route('/upload', methods=['POST'])
    def uploadFile():
        if 'file' not in request.files:
            return jsonify({'error': 'Missing file parameter'}), 400
        file = request.files['file']
        
        id_column_name = request.form.get('id_column_name')
        title_column_name = request.form.get('title_column_name')
        user_id = request.remote_addr
        
        result = UploadFileService.uploadFile(file, id_column_name, title_column_name, user_id)
        if 'error' in result:
            return jsonify(result), 400
        return jsonify(result), 200

    @app.route('/recommend', methods=['GET'])
    def getRecommendations():
        data = request.get_json()

        id = data.get('id')
        quantity = data.get('quantity')
        file_name = data.get('file_name')
        user_id = GetClientIP.getClientIP(request)
        if user_id is None:
            return jsonify({'error': 'Unable to get user IP'}), 400
        
        recommendations = ListRecommendationsService.listRecommendations(id, quantity, user_id, file_name)
        if 'error' in recommendations:
            return jsonify(recommendations), 400
        return jsonify({'recommendations': recommendations}), 200
    
    
    @app.route('/files', methods=['GET'])
    def listFiles():
        user_id = GetClientIP.getClientIP(request)

        list_files = ListFilesService.listFiles(user_id)
        if 'error' in list_files:
            return jsonify(list_files), 404
        return jsonify(list_files), 200
    
    
    @app.route('/delete', methods=['DELETE'])
    def deleteFile():
        data = request.get_json()
        
        file_name = data.get('file_name')
        user_id = GetClientIP.getClientIP(request)
        
        result = DeleteFileService.deleteFile(user_id, file_name)
        if 'error' in result:
            return jsonify(result), 400
        return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
