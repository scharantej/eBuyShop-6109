
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.00},
    {'id': 2, 'name': 'Product 2', 'price': 15.00}
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products, cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    product = [p for p in products if p['id'] == int(product_id)][0]
    cart.append(product)
    flash('Product added to cart')
    return redirect(url_for('index'))

@app.route('/checkout', methods=['POST'])
def checkout():
    name = request.form.get('name')
    address = request.form.get('address')
    payment = request.form.get('payment')
    flash('Thank you for your purchase!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
