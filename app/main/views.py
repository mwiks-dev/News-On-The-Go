from flask import render_template,request,redirect,url_for
from . import main
from  requests import get_sources, get_article

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    sources = get_sources()
    title = f'{sources.title}'

    return render_template('index.html',title = title, sources = sources)

@main.route('/movie/<int:id>')
def get_article(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('artticles.html',title = title,article=article)