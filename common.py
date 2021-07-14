import requests
import os
#Reddit App
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

#send request for oauth token
oath_res =  requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = oath_res.json()['access_token']
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

#list of websites
list_of_subreddits = {
  'MEMES': "https://oauth.reddit.com/r/memes/new",
  'FUNNY': "https://oauth.reddit.com/r/funny/new"
}

#list of channels
list_of_channels = {
  'TEST' : 862116430547124245,
  'TEST2' : 864745265004544040
}

#get json from reddit and write the part needed into all_json and returns it
def get_new_Threads(urlKey):
  all_json = []
  res = requests.get(list_of_subreddits[urlKey], headers=headers, params={'limit':'1'})
  print(res)
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

#temp second
#probably more concise way to do this
# def get_new_bapcsThreads():
#   all_json = []
#   res = requests.get("https://oauth.reddit.com/r/memes/new", headers=headers, params={'limit':'1'})
#   for post in res.json()['data']['children']:
#     if post['kind'] == 't3':
#       title = post['data']['title']
#       url = post['data']['url']
#       cur_json = {
#         "title" : title,
#         "url" : url
#       }
#       all_json.append(cur_json)
#   return all_json



#format of the post
#how do you generalize it?
#got error with function in parameter, instanciate error?
def get_first_threads(urlKey):
  postdata = get_new_Threads(urlKey)[0]
  redpost = "[Post]: " + postdata['title'] + "\n" + postdata['url'] 
  return redpost
