from flask import render_template,request,redirect,url_for
from . import main
from  ..requests import get_sources, get_article

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

@main.route('/movie/<int:id>')
def articles(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article(id)
    

    return render_template('artticles.html',article=article)