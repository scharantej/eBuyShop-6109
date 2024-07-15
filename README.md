## HTML Files

### index.html
**Use:** Main page of the website, displaying available products and allowing users to add them to their carts.
**Content:**

```html
<h1>Welcome to Our Store</h1>

<div id="products">
  <!-- Dynamically generated list of products using Flask's render_template() -->
</div>

<div id="cart">
  <!-- Dynamically generated cart display using Flask's render_template() -->
</div>
```

### checkout.html
**Use:** Page where users can finalize their purchases and enter payment information.
**Content:**

```html
<h1>Checkout</h1>

<form action="/checkout">
  <label for="name">Name:</label>
  <input type="text" name="name">
  <br>
  <label for="address">Address:</label>
  <input type="text" name="address">
  <br>
  <label for="payment">Payment Method:</label>
  <select name="payment">
    <option value="credit_card">Credit Card</option>
    <option value="debit_card">Debit Card</option>
    <option value="paypal">PayPal</option>
  </select>
  <br>
  <input type="submit" value="Purchase">
</form>
```

## Routes

### /products
**Purpose:** Endpoint to fetch available products to display on the main page.
**Method:** GET
**Returns:** JSON response with a list of products in the format:

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 10.00
  },
  {
    "id": 2,
    "name": "Product 2",
    "price": 15.00
  }
]
```

### /add_to_cart
**Purpose:** Endpoint to add a product to the user's cart.
**Method:** POST
**Arguments:** `product_id`
**Returns:** JSON response with the updated cart in the format:

```json
{
  "cart": [
    {
      "id": 1,
      "name": "Product 1",
      "quantity": 1
    },
    {
      "id": 2,
      "name": "Product 2",
      "quantity": 1
    }
  ]
}
```

### /checkout
**Purpose:** Endpoint to handle the checkout process and save the order.
**Method:** POST
**Arguments:** User information and payment details
**Returns:** Redirect to a "Thank you for your purchase" page.