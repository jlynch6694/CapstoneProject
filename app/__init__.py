from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

#application variables
app=Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#outes must be imported after app variable is set
from app import routes
