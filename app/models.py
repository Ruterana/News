class Sources:
    '''
    newssource class to define news Objects
    '''

    def __init__(self, id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
#####for articles#############
class Articles:
    '''
    newsArticle class to define news oblects
    '''
    def __init__(self,id,name,author,title,description,url,urlToImage,publicedAt,content)
         self.id = id
         self.name = name
         self.author = author
         self.title = title
         self.description = description
         self.url = url
         self.urlToImage = urlToImage
         self.publicedAt = publicedAt
         self.content = content
