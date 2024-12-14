from flask import Blueprint, jsonify
from app.services.lora_service import send_lora_request

blueprint = Blueprint('node', __name__)

@blueprint.route('/all_node_data', methods=['GET'])
def all_node_data():
    response, status_code = send_lora_request('get', "/all_node_data")
    return jsonify(response), status_code

@blueprint.route('/get_node_data/<int:node_id>', methods=['GET'])
def get_node_data(node_id):
    response, status_code = send_lora_request('get', f"/node_data/{node_id}")
    return jsonify(response), status_code
