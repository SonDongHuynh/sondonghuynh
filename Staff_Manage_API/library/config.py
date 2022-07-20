import os
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'sondongh113@gmail.com'
MAIL_PASSWORD = 'yoxmfrpccohthujd'
MAIL_USE_SSL = True

