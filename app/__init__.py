from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.logger import configure_logging
from app.tasks.scheduler import configure_scheduler
from app.routes import periodic, tank, node

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure logging
    configure_logging()

    # Register Blueprints
    app.register_blueprint(periodic.blueprint)
    app.register_blueprint(tank.blueprint)
    app.register_blueprint(node.blueprint)

    # Configure Scheduler
    scheduler = BackgroundScheduler()
    configure_scheduler(scheduler)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    return app

app = create_app()

