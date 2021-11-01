import urllib.request,json
from .models import sources
from .models import articles
Source = sources.Source
Articles = articles.Articles

# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCES_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        category = sources_item.get('category')
        country = sources_item.get('country')
        language = sources_item.get('language')
       
        if id:
            sources_object = Source(id,category,country,language)
            sources_results.append(sources_object)

    return sources_results


def get_article(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            image = article_details_response.get('image_url')
            description = article_details_response.get('description')
            author = article_details_response.get('author')
            published_at = article_details_response.get('published_at')

            article_object = Articles(id,image,description,author,published_at)

    return article_object