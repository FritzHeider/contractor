from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

host = os.environ.get('MONGODB_URI', "mongodb://heroku_wm6zd8jl:j4v47b6f6i4ba17b9b712qf8hn@ds333238.mlab.com:33238/heroku_wm6zd8jl")
#host = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/contractor")

client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()
items = db.items
cart = db.cart


@app.route("/")
def items_index():
    """Return homepage"""
    return render_template("items_index.html", items=items.find())


@app.route("/cart")
def cart_show():
    """Show the user's cart"""
    return render_template("cart_show.html", cart=cart.find())


@app.route("/cart/<item_id>")
def cart_item_show(item_id):
    """Show a single item in a user's cart"""
    item = cart.find_one({"_id": ObjectId(item_id)})
    return render_template("cart_item_show.html", item=item)


@app.route("/cart/<item_id>/delete", methods=["POST"])
def cart_delete(item_id):
    """Delete an item from the user's cart"""
    cart.delete_one({"_id": ObjectId(item_id)})
    return redirect(url_for("cart_show"))


@app.route("/cart/destroy")
def cart_destroy():
    """Delete all items in a user's cart"""
    for item in cart.find():
        cart.delete_one({"_id": ObjectId(item["_id"])})
    return redirect(url_for("cart_show"))


@app.route("/cart/checkout")
def cart_checkout():
    """Allow the user to checkout"""
    total = 0
    for item in cart.find():
        total += int(item["price"])
    print("$" + str(total))
    return redirect(url_for("cart_destroy"))


@app.route("/items/new")
def new_item():
    """Return new item creation page"""
    return render_template("items_new.html", item={},
                           title='New item')


@app.route("/items/new", methods=["POST"])
def items_new():
    """Allow the user to create a new item"""
    item = {
        "name": request.form.get("name"),
        "price": request.form.get("price"),
        "image": request.form.get("image")
    }
    item_id = items.insert_one(item).inserted_id
    return redirect(url_for("items_show", item_id=item_id))


@app.route("/items/<item_id>")
def items_show(item_id):
    """Show a single item."""
    item = items.find_one({"_id": ObjectId(item_id)})
    return render_template("items_show.html", item=item)


@app.route('/items/<item_id>', methods=['POST'])
def items_update(item_id):
    """Submit an edited item."""
    updated_item = {
        'title': request.form.get('title'),
        'price': request.form.get('price'),
        'image': request.form.get('image')
    }
    items.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': updated_item})
    return redirect(url_for('items_show', item_id=item_id))


@app.route("/items/<item_id>/edit")
def items_edit(item_id):
    """Show the edit form for a item."""
    item = items.find_one({"_id": ObjectId(item_id)})
    return render_template("items_edit.html", item=item,
                           title="Edit item")


@app.route('/items/<item_id>/delete', methods=['POST'])
def items_delete(item_id):
    """Delete one item."""
    items.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('items_index'))


@app.route('/items/<item_id>/add-to-cart', methods=['POST'])
def add_to_cart(item_id):
    """Add an item to the user's cart"""
    item = items.find_one({"_id": ObjectId(item_id)})
    for _ in range(int(request.form.get("quant"))):
        new_item = {
            "name": item["name"],
            "price": item["price"],
            "image": item["image"]
        }
        cart.insert_one(new_item)
    return redirect(url_for('cart_show'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
