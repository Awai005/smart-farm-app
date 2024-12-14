from flask import Blueprint, jsonify
from app.services.lora_service import send_lora_request
from app.models import NodeData
from app import db

blueprint = Blueprint('periodic', __name__)

@blueprint.route('/periodic_data/<int:node_id>', methods=['GET'])
def periodic_data(node_id):
    response, status_code = send_lora_request('get', f"/periodic_data/{node_id}")
    if status_code != 200:
        return jsonify({"status": "error", "message": "Failed to fetch data"}), status_code

    data = response

    if data:
        # Save data to the database
        new_entry = NodeData(
            node_id=data[0],
            moisture=data[1],
            humidity=data[2],
            temperature=data[3],
            pump_status=data[4]
        )
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Data fetched and saved to the database",
            "data": {
                "node_id": data[0],
                "moisture": data[1],
                "humidity": data[2],
                "temperature": data[3],
                "pump_status": data[4]
            }
        }), 200
    else:
        return jsonify({"status": "error", "message": "No data to save"}), 400
