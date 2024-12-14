from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.services.lora_service import send_lora_request
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def scheduled_periodic_data():
    node_ids = [1, 2]  # Replace with your actual node IDs
    for node_id in node_ids:
        logger.info(f"Fetching periodic data for Node {node_id}")
        response, status_code = send_lora_request('get', f"/periodic_data/{node_id}")
        if status_code == 200:
            logger.info(f"Periodic data for Node {node_id}: {response}")
        else:
            logger.error(f"Failed to fetch periodic data for Node {node_id}: {response}")

scheduler.add_job(
    func=scheduled_periodic_data,
    trigger=IntervalTrigger(minutes=30),
    id='fetch_periodic_data',
    name='Fetch periodic data for all nodes every 30 minutes',
    replace_existing=True
)
