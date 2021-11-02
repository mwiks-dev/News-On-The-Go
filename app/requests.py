import urllib.request,json
from models import Source
from models import Articles


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
    get_sources_url = 'https://newsapi.org/v2/sources?apiKey=94d343343a714ec2b5f6a024996fe7d2'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)


    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        category = sources_item.get('category')
        country = sources_item.get('country')
        language = sources_item.get('language')
       
        if id:
            sources_object = Source(id,name,category,country,language)
            sources_results.append(sources_object)

    return sources_results


def process_articles(articles_list):
    '''
    Function that processes the articles result and transform them to a list of objects

    Args:
        articles_list:A list of dictionaries that contains articles details

    Returns:
         articles_results:A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        imageUrl = articles_item.get('imageUrl')
        description = articles_item.get('description')
        author = articles_item.get('author')
        publishedAt = articles_item.get('publishedAt')
        url = articles_item.get('url')

        if imageUrl:
            articles_object = Articles(title,description,imageUrl,author,publishedAt,url)
            articles_results.append(articles_object)

    return articles_results

def get_articles(sources_name):
    '''
    Function that gets the json results to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(sources_name,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results