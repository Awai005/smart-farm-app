import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql://postgresql_smart_farm_user:qzeonyxkLVTORJwXSylxJAYlmkf9rlZR@dpg-ctenlf52ng1s738d2bu0-a/postgresql_smart_farm", "postgresql://postgresql_smart_farm_user:qzeonyxkLVTORJwXSylxJAYlmkf9rlZR@dpg-ctenlf52ng1s738d2bu0-a:5432/postgresql-smart-farm")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
