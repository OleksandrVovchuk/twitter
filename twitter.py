import oauth2
import hidden
import json


def oauth_req(url, http_method="GET", http_headers=None):
    '''
    (url) -> (file.json)
    Returns json file of Twitter API
    '''

    secrets = hidden.oauth()
    consumer = oauth2.Consumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth2.Token(secrets['token_key'], secrets['token_secret'])
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, headers=http_headers )
    return content
def main(name,n,atribute1,atribute2,people):
    '''
    (str,int,str) -> (list of sets)
    Returns list of tuples with different atributes
    atributes: name, screen_name, location, created_at ...
    '''

    if people == 'friends':
        url = 'https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=' + str(name) + '&count=' + str(n)
    elif people == 'followers':
        url = 'https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=' + str(name) + '&count=' + str(n)
    else:
        print('Bad request')
        return None
    data = oauth_req(url)
    t = json.loads(data)
    info=[]
    for user in t['users']:
        info.append((user[atribute1],user[atribute2]))
    return info
