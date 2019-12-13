from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
from datetime import datetime
from markov import generate_sentence
from sampling import sample, histogram


app = Flask(__name__)

host = os.environ.get('MONGODB_URI', "mongodb://heroku_wm6zd8jl:j4v47b6f6i4ba17b9b712qf8hn@ds333238.mlab.com:33238/heroku_wm6zd8jl")
host = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")

client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()
items = db.items
cart = db.cart


@app.route('/')
def index():
	return render_template('index.html', sentence=generate_sentence())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
