from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static') 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/read/')
def read():
    return render_template('read.html')

@app.route('/read/<review_id>/')
def read(review_id):
    return render_template('review.html')
