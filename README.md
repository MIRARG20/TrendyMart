# TrendyMart

![TrendyMart Screenshot](TrendyMart/screenshot-homepage.png)

## Project Overview

TrendyMart is a solo project developed as an e-commerce website where users can create accounts, browse and purchase products, and complete transactions using Visa, MasterCard, or PayPal. The platform supports account creation, shopping cart functionality, order total calculations, and shipping to user addresses.

## Team

This project was developed by:
- **Amira Ragab** - [amiraragab480@gmail.com](mailto:amiraragab480@gmail.com)

## Technologies

- **Frontend**: HTML, CSS
- **Backend**: Python Flask
- **Database**: MySQLAlchemy
- **Payment Integration**: Visa, MasterCard, PayPal

## Infrastructure

The application is built on a Flask server with a MySQL database backend. It is designed to handle user authentication, product management, shopping cart operations, and payment processing.


## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MIRARG20/TrendyMart.git
   ```
2. **Install dependencies:**
   ```bash
   cd TrendyMart
   pip install -r requirements.txt
   ```
3. **Set up the database:**
   - Create a MySQL database and update the database configuration in `config.py`.
   ```python
   DATABASE_URI = 'mysql+pymysql://username:password@localhost/trendymart'
   ```
   - Run migrations to set up the tables.
   ```bash
   flask db upgrade
   ```
4. **Run the application:**
   ```bash
   flask run
   ```
5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, amiraragab480@gmail.com.