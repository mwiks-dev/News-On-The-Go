from flask import render_template
from . import main
from  ..requests import get_sources, get_articles

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    sources = get_sources()
    title = 'Welcome to News OTG'

    return render_template('index.html',title = title, sources = sources)

@main.route('/articles/<sources_name>')
def articles(sources_name):
    '''
    View articles page function that returns the  article details page and its data
    '''
    articles = get_articles(sources_name)
    print(articles)

    

    return render_template('articles.html',articles = articles)