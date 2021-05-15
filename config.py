import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
#SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgresql@localhost:5432/fyyur'
#SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost:5432/<database_name>'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#FLASK_ENV=development