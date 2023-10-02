from flask import Flask

from app_formulaire.config import Config

app = Flask(__name__)
app.config.from_object(Config)
from app_formulaire import routes