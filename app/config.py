import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_HOST = os.getenv("DB_HOST")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")

    SQLALCHEMY_DATABASES_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}/{DB_HOST}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    FLASK_JWT_SECRET_KEY= os.getenv("FLASK_JWT_SECRET_KEY")
    