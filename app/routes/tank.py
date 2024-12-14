from flask import Blueprint, jsonify, request
from app.services.lora_service import send_lora_request

bp = Blueprint('tank', __name__)

@bp.route('/tank_data/<int:node_id>', methods=['GET'])
def tank_data(node_id):
    response, status_code = send_lora_request('get', f"/tank_data/{node_id}")
    return jsonify(response), status_code

@bp.route('/set_threshold/<int:node_id>', methods=['POST'])
def set_threshold(node_id):
    data = request.get_json()
    if not data or "threshold" not in data:
        return jsonify({"status": "error", "message": "Threshold not provided"}), 400

    try:
        threshold = int(data.get("threshold"))
    except (ValueError, TypeError):
        return jsonify({"status": "error", "message": "Threshold must be an integer"}), 400

    response, status_code = send_lora_request('post', f"/set_threshold/{node_id}", json={"threshold": threshold})
    return jsonify(response), status_code
