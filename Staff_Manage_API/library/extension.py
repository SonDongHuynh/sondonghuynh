from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_mail import Mail,Message

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()

