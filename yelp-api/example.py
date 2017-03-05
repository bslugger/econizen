import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

endpoint_base = 'https://api.yelp.com/v3'
app_id = os.environ.get('YELP_APP_ID', None)
app_secret = os.environ.get('YELP_APP_SECRET', None)

client = BackendApplicationClient(client_id=app_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.yelp.com/oauth2/token',
        client_id=app_id, client_secret=app_secret)

# print(token)
# print(oauth.request)

params = {}
# params['term'] = 'test'
params['location'] = 'SanFrancisco'
r = oauth.request('GET', endpoint_base + '/businesses/search?term=test&location=San Francisco')

print r.json()
