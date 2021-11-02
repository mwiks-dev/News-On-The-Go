class Sources:
    '''
    News Sources class to define news source objects
    '''

    def __init__(self,id,name,category,description):
        self.id = id
        self.name = name
        self.category = category
        self.description = description

class Articles:
    '''
    News Articles class to define news articles objects
    '''
    def __init__(self,title,urlToImage,author,publishedAt,url):
        self.title = title
        self.urlToImage = urlToImage
        self.author = author
        self.publishedAt= publishedAt
        self.url=url