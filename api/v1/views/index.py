#!/usr/bin/python3
"""Index.py"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    return jsonify(status="OK")


@app_views.route('/stats')
def stat():
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    counter = {}
    for cls in classes:
        counter[cls] = storage.count(classes[cls])
    return jsonify(counter)
