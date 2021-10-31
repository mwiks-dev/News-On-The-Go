import urllib.request,json
from .models import NewsSource
from .models import NewsArticles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        status = news_item.get('status')
        totalResults = news_item.get('totalResults')
        articles = news_item.get('articles')
       
        if status:
            news_object = NewsSource(status, totalResults, articles)
            news_results.append(news_object)

    return news_results


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

            article_object = NewsArticles(id,image,description,author,published_at)

    return article_object