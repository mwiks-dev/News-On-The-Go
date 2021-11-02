class Source:
    '''
    News Source class to define news source objects
    '''

    def __init__(self,id,name,category,country,language):
        self.id = id
        self.name = name
        self.category = category
        self.country = country
        self.language = language

class Articles:
    '''
    News Articles class to define news articles objects
    '''
    def __init__(self,title,image,description,author,publishedAt,url):
        self.title = title
        self.image = image
        self.description = description
        self.author = author
        self.publishedAt= publishedAt
        self.url=url