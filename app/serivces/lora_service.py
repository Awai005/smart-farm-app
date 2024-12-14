import requests
import logging

LORA_SERVICE_URL = "https://40ce-124-111-21-208.ngrok-free.app"
logger = logging.getLogger(__name__)

def send_lora_request(method, endpoint, **kwargs):
    url = f"{LORA_SERVICE_URL}{endpoint}"
    try:
        response = requests.request(method, url, timeout=10, **kwargs)
        response.raise_for_status()
        logger.info(f"Successful {method.upper()} request to {url}")
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during {method.upper()} request to {url}: {e}")
        return {"status": "error", "message": str(e)}, 500
