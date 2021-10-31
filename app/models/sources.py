class NewsSource:
    '''
    News Source class to define news source objects
    '''

    def __init__(self,status,totalResults,articles):
        self.status = status
        self.totalResults = totalResults
        self.articles = articles
