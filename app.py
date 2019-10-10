from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient



client = MongoClient()
db = client.items
items = db.items

app = Flask(__name__)
#
#
# items = [
#    { 'title': 'Great item' },
#    { 'title': 'Next item' }
#  ]

@app.route('/')
def items_index():
    """Show all items."""
    return render_template('items_index.html', items=items.find())

# @app.route('/cart')
# def cart():
#     """display user's shopping cart"""
#     return render_template('cart.html', items=items.find())

@app.route('/items/new')
def items_new():
    """Create a new item."""
    return render_template('items_new.html')




    @app.route('/thanks')
    def items_index():
        """Show all items."""
        return render_template('items_index.html', items=items.find())

@app.route('/items', methods=['POST'])
def items_submit():
    """Submit a new item."""
    print(request.form.to_dict())
    return redirect(url_for('items_index'))
