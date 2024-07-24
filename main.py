from flask import Flask, render_template, request, redirect, url_for, flash\nfrom flask_sqlalchemy import SQLAlchemy\n\napp = Flask(__name__)\napp.config['SECRET_KEY'] = 'secret-key'\n\nproducts = [\n    {'id': 1, 'name': 'Product 1', 'price': 10.00},\n    {'id': 2, 'name': 'Product 2', 'price': 15.00}\n]\n\ncart = []\n\n@app.route('/')\ndef index():\n    total = sum([item['price'] for item in cart])\n    return render_template('index.html', products=products, cart=cart, total=total)\n\n@app.route('/add_to_cart', methods=['POST'])\ndef add_to_cart():\n    product_id = request.form.get('product_id')\n    product = [p for p in products if p['id'] == int(product_id)][0]\n    cart.append(product)\n    flash('Product added to cart')\n    return redirect(url_for('index'))\n\n@app.route('/checkout', methods=['POST'])\ndef checkout():\n    name = request.form.get('name')\n    address = request.form.get('address')\n    payment = request.form.get('payment')\n    flash('Thank you for your purchase!')\n    return redirect(url_for('index'))