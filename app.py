from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='What are we selling!')

items = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird', 'img': 'img src="https://via.placeholder.com/150', 'in_cart' : TRUE },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]
@app.route('/items')
def itemss_index():
    """Show all items."""
    return render_template('items.html', items=items)

@app.route('/cart')
def cart():
    """display user's shopping cart"""
    return render_template('cart.html', items=items.find())
