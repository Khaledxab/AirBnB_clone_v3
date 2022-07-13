#!/usr/bin/python3
"""Index.py"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """_summary_
    Returns:
    _type_: _description_
    """
    return jsonify(status="OK")


@app_views.route('/stats')
def stat():
    """_summary_
    Returns:
        _type_: _description_
    """    
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

if __name__ == "__main__":
    pass
