from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources
# Views
@main.route('/')
def index():
    return render_template('index.html')
    '''
    View root page function that returns the category page and its data
    '''

    # Getting get source
    category_sources = get_sources('category')
    print(category_sources)
    title = 'Home - Welcome to The best news resources Website Online'
    return render_template('index.html', title = title, category = category_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )