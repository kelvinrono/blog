import requests,json
from .models import Quote

# Getting the quote base url
base_url=None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']
    
def getQuotes(): 
    # request.urlopen(base_url):
        
        res = requests.get(base_url).json()
       
        response = []
        id = res.get('id')
        author = res.get('author')
        quote = res.get('quote')

        quoteObject = Quote(id,author,quote)
        response.append(quoteObject)
        return response