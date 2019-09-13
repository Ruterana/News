import os

class Config:

    SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    SOURCE_API_KEY = 'ad6606b55c7d4d83bf3cd45680c71637'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    print(SOURCE_API_KEY)

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
###### for article#########
ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?domains=wsj.com,nytimes.com&apiKey={}'
ARTICLE_API_KEY = 'ad6606b55c7d4d83bf3cd45680c71637'
SECRET_KEY = os.environ . get ('SECRET_KEY')
print (ARTICLE_API_KEY )
