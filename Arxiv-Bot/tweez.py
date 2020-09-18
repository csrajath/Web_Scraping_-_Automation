import tweepy
from datetime import *

c_key = '4hC9b6O0gfl1AnEXyWYaTPp6D'
c_secret = '1DS93LurEzMCydu8wICVQSgUmr6P6a8LGXCIX7PnQvqfugOT0c'


auth = tweepy.AppAuthHandler(c_key, c_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

   
urls=[]
end_date = datetime.utcnow() - timedelta(days=1)
print(end_date)
for status in tweepy.Cursor(api.user_timeline, id='arxiv_org').items():

    if hasattr(status, "entities"):
        entities = status.entities
        urls.append(entities['urls'][0].get('expanded_url'))
    if status.created_at < end_date:
        break

