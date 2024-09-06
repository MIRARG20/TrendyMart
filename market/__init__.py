from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'cf5f0f62470c270ccfd3c7d5'
db = SQLAlchemy(app)

from market import routes





# if __name__ == '__main__':
#     app.run(debug=True, port=9000)





# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True, port=9000)