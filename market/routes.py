from market import app
from flask import render_template,redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm
from market import db

# Route for the indexpage
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html', title="About")

# Route for the products page
@app.route('/products')
def products():
    return render_template('products.html', title="Products")

# Route for the market page
@app.route('/market')
def market():
    # Query all items from the database
    items = Item.query.all()
    return render_template('market.html', title="market", items=items)


# Routes for product details pages
@app.route('/products-details')
def products_details():
    return render_template('products-details.html', title="products-details")


@app.route('/products-details2')
def products_details2():
    return render_template('products-details2.html', title="products-details2")

@app.route('/products-details3')
def products_details3():
    return render_template('products-details3.html', title="products-details3")

# Route for the offer page
@app.route('/offer')
def offer():
    return render_template('offer.html', title="offer")

# Route for account creation (GET and POST methods)
@app.route('/account', methods=['GET', 'POST'])
def account():
    # Create an instance of the RegisterForm
    form = RegisterForm()
    # Check if the form has been submitted and validated successfully
    if form.validate_on_submit():
        # Create a new User instance based on form data
        user_to_create = User(username=form.username.data, 
                            email_address=form.email_address.data,
                            password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        # Redirect to the index page after successful registration
        return redirect(url_for('index'))

    # Check if there are any validation errors in the form
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with Creating a User: {err_msg}')
    return render_template('account.html', form=form, title="account")


# Route for the cart page
@app.route('/cart')
def cart():
    return render_template('cart.html', title="cart")