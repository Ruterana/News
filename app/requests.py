import urllib.request,json
from.models import Source
# Getting api key
api_key = None
#Getting the news base url
base_url= None
def configure_request(app):
    global api_keybase_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_getsources_response['results']
            getsources_results = process_results(movie_results_list)


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
        name = sources_item ('name')
        description =sources_item.get ('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        if poster:
            sources_object = sources(id,name,description,url,category,language,country)
            sources_results.append(sources_object)

    return sources_results

