from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the category page and its data
    '''

    # Getting get source
    category_sources = get_sources('general')
    print(category_sources)
    title = 'Welcome to The news resources '
    return render_template('index.html', title = title, category_sources = category_sources)