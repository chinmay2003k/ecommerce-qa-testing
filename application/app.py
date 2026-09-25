
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "qa-testing-project"

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Wireless Mouse", "price": 800},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Headphones", "price": 2500}
]


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "testuser" and password == "Test@123":
            session["user"] = username
            return redirect(url_for("products"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


@app.route("/products")
def products():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("products.html", products=PRODUCTS)


@app.route("/cart")
def cart():
    if "user" not in session:
        return redirect(url_for("login"))

    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    if "user" not in session:
        return redirect(url_for("login"))

    product = next(
        (item for item in PRODUCTS if item["id"] == product_id),
        None
    )

    if product:
        cart = session.get("cart", [])
        cart.append(product)
        session["cart"] = cart

    return redirect(url_for("products"))


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "user" not in session:
        return redirect(url_for("login"))

    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)

    if request.method == "POST":
        session.pop("cart", None)
        return render_template(
            "checkout.html",
            success="Order placed successfully!"
        )

    return render_template(
        "checkout.html",
        cart_items=cart_items,
        total=total
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)


