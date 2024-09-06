from market import app
from flask import render_template,redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/products')
def products():
    return render_template('products.html', title="Products")
@app.route('/market')
def market():
    items = Item.query.all()

    return render_template('market.html', title="market", items=items)

@app.route('/products-details')
def skills():
    return render_template('products-details.html', title="products-details")

@app.route('/account', methods=['GET', 'POST'])

def account():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, 
                            email_address=form.email_address.data,
                            password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors != {}: #if there are not errors from the validation
        for err_msg in form.errors.values():
            flash(f'There was an error with Creating a User: {err_msg}')

    return render_template('account.html', form=form, title="account")

@app.route('/cart')
def cart():
    return render_template('cart.html', title="cart")