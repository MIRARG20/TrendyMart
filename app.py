from flask import Flask, render_template

app = Flask(__name__)
my_skills = [('javascript',85), ('php',30) ,('python', 75), ('Mysql',90), ('sql',45)]

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/products')
def products():
    return render_template('products.html', title="Products")

@app.route('/products-details')
def skills():
    return render_template('products-details.html', title="products-details", page_head='My_skills')

@app.route('/account')
def account():
    return render_template('account.html', title="account")

@app.route('/cart')
def cart():
    return render_template('cart.html', title="cart")


if __name__ == '__main__':
    app.run(debug=True, port=9000)

