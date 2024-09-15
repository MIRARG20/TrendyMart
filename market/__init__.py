from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create a new Flask application instance
app = Flask(__name__)

# Configure the database URI for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# Set a secret key for security
app.config['SECRET_KEY'] = 'cf5f0f62470c270ccfd3c7d5'

# Initialize SQLAlchemy with the Flask application
db = SQLAlchemy(app)

from market import routes

