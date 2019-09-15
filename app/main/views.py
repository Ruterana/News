from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

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
    
@main.route('/articles/<id>')
def articles(id):
    '''
    view root page  function that returns the category page and its data
    '''
    #getting get articles
    articles = get_articles(id)
    print (articles)
    title = 'top articles'
    return render_template('articles.html',title = title,articles = articles)
