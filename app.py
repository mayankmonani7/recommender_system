# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:57:26 2021

@author: MAYANK MONANI
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import recommender

app = Flask(__name__)
CORS(app) 
        
@app.route('/movie', methods=['GET'])
def recommend_movies():
    res = recommender.results(request.args.get('title'))
    return jsonify(res)

if __name__=='__main__':
    app.run(port = 5000, debug = True)