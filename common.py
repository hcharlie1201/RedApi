import requests
import os

CLIENT_ID = 'ZfoP0aiFdAO6f63GBzr8CA'
SECRET_KEY = 'bRUhJHOumx8mjxiSB_nPIVeyeNV9cw'

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)#authorization
#login
data = {
  'grant_type' : 'password',
  'username' : 'hcharlie1201',
  'password' : os.environ['pw']
}
#to check version
headers = {'User-Agent' : 'MyApi/0.0.1'}
twords = ["test"]
#send request for oauth token
oath_res =  requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = oath_res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}



def get_new_threads():
  all_json = []
  res = requests.get("https://oauth.reddit.com/r/buildapcsales/new", headers=headers, params={'limit': '1'})
  for post in res.json()['data']['children']:
    if post['kind'] == 't3':
      title = post['data']['title']
      url = post['data']['url']
      cur_json = {
        "title" : title,
        "url" : url
      }
      all_json.append(cur_json)
  return all_json

def get_first_threads():
  postdata = get_new_threads()[0]
  redpost = postdata['title'] + "\n" + postdata['url'] 
  return redpost
1