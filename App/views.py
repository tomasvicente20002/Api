"""
Routes and views for the flask application.
"""

from datetime import datetime
from App import app
from flask import jsonify
from App.Tables import voos


@app.route('/')
@app.route('/home')
def home():

    table = voos.Voos()
    table.name = '12'
    """Renders the home page."""
    return {
        'title':'Home Page',
        'year':datetime.now().year,
        'table.name': table.name 
    }
    

@app.route('/contact')
def contact():
    """Renders the contact page."""

    return {
        'title':'Contact',
        'year':datetime.now().year,
        'message':'Your contact page.'
    }


@app.route('/about')
def about():
    """Renders the about page."""
    return {
        'title':'About',
        'year':datetime.now().year,
        'message':'Your application description page.'
    }
