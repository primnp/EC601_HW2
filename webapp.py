from flask import Flask, request, render_template, jsonify, request, redirect, url_for
from flask_restful import Resource, Api
import os
import json
import logging
import social_analyzer as sa

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return redirect(url_for('sa_home'))

# home page
@app.route('/soc-analyze')
def sa_home():
    return '''
        <h1>Social Analyzer</h1>
        <p>Please refer to readme.md on how to use this social analyzer</p>
    '''

# retrieve a specified number of tweets from a user
@app.route('/soc-analyze/<string:username>/<int:nooftweets>')
def analyze_twtusers(username, nooftweets):
    res = dict()
    res["Results"] = sa.twitter_retrieve(username, nooftweets)
    return res

# retrieve sentiment scores of a specified number of tweets from a user
@app.route('/soc-analyze/<string:username>/<int:nooftweets>/sentiments')
def analyze_twtsentiments(username, nooftweets):
    arr = sa.twitter_retrieve(username, nooftweets)
    res = dict()
    res["Results"] = sa.entities_sentiments_retrieve(arr)
    return res

@app.route('/soc-analyze/<string:username>/<int:nooftweets>/hashtag/<string:hashtag>')
def findfrom_hashtag(username, nooftweets, hashtag):
    arr = sa.twitter_retrieve(username, nooftweets)
    arr2 = sa.entities_sentiments_retrieve(arr)
    res = dict()
    res["Results"] = sa.txt_hashtag_retrieve(hashtag, arr2)
    return res


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port = 5000)
