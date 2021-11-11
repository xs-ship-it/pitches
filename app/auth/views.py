from flask import render_template
from . import main

@main.route('/')
def index():
    """
    view root page function
    """
    title = 'pitches'
    return render_template('index.html',title=title)