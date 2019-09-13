import urllib.request,json
from .models import Sources
from .models import Articles
# Getting api key
api_key = None
#Getting the news base url
base_url= None
def configure_request(app):
    global api_key, base_url
    api_key = app.config['SOURCE_API_KEY']
    print(api_key)
    base_url = app.config['SOURCES_API_BASE_URL']
    bases_url = app.config['ARTICLE_API_BASE_URL'] 
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    print('charlene')
    

    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
    sources_list: A list of dictionaries that contain movie details

    Returns :
    sources_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description =sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        if name:
            sources_object = Sources(id,name,description,url,category,language,country)
            sources_results.append(sources_object)

    return sources_results
def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = Process_results(articles_results_list)


    return articles_results
def Proces_results(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
    articles_list: A list of dictionaries that contain articles details

    Returns :
    sources_results: A list ofarticles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        
        id = articles_item.get('id')
        name = articles_item.get('name')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publicedAt = articles_item.get('publicedAt')
        content = articles_item.get('content')
        if name:
            articles_object = Sources(id,name,author,title,description,url,urlToImage,publicedAt,content)
            articles_results.append(articles_object)

    return articles_results