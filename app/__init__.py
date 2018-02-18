
from flask import Flask, render_template
from flask_environments import Environments

app = Flask(__name__)

# Recuperation des données de paramétrages de l'application
# Shell variable creation  :  $ export FLASK_ENV="DevelopmentConfig"
# TODO : [MODERNISATION] utilisation d'un fichier YAML

env = Environments(app, var_name='FLASK_ENV', default_env='TestConfig')
env.from_object('config')


from app.utils import logmanager
