class NewsArticles:
    '''
    News Articles class to define news articles objects
    '''
    def __init__(self,id,image,description,author,published_at):
        self.id = id
        self.image = image
        self.description = description
        self.author = author
        self.published_at= published_at