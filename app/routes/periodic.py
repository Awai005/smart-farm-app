from flask import Blueprint, jsonify
from app.services.lora_service import send_lora_request

bp = Blueprint('periodic', __name__)

@bp.route('/periodic_data/<int:node_id>', methods=['GET'])
def periodic_data(node_id):
    response, status_code = send_lora_request('get', f"/periodic_data/{node_id}")
    return jsonify(response), status_code
