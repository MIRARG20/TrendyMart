<!-- landing page for my the portfolio project -->

# TrendyMart
![TrendyMart Screenshot](screenshot/screenshot4.png)
![TrendyMart Screenshot](screenshot/screenshot1.png)


## Project Overview

TrendyMart is a solo project developed as an e-commerce website where users can create accounts, browse and purchase products, and complete transactions using Visa, MasterCard, or PayPal. The platform supports account creation, shopping cart functionality, order total calculations, and shipping to user addresses.
![TrendyMart Screenshot](screenshot/screenshot2.png)

## Team
![TrendyMart Screenshot](screenshot/screenshot5.png)

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

Follow these steps to get started with the project:

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
   ```python
   DATABASE_URI = 'mysql+pymysql://username:password@localhost/trendymart'
   ```
   ```bash
   flask db upgrade
   ```
4. **Run the application:**
   ```bash
   flask run
   ```
5. **Access the application:**
   Navigate to `http://localhost:5000`.


## Contact

For any questions or feedback, amiraragab480@gmail.com.
