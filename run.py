# Import the Flask application instance from the market module
from market import app


if __name__ == '__main__':
    app.run(debug=True)