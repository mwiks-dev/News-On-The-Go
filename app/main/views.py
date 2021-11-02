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
    title = 'News OTG'

    return render_template('index.html',title = title, sources = sources)

@main.route('/articles/<sources_id>')
def articles(sources_id):
    '''
    View articles page function that returns the  article details page and its data
    '''
    articles = get_articles(sources_id)
    
    return render_template('articles.html',articles = articles)