from app import app, db

# Initialize the database
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
