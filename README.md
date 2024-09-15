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

## License

This project is licensed under the MIT License. See below for details:

MIT License

Copyright (c) [2024] [Amira Ragab Mohamed]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Contact

For any questions or feedback, amiraragab480@gmail.com.
