import twitter

api = twitter.Api(consumer_key='M5dA1RDP8n3xqaWpf7x3aOn9c', consumer_secret='6WfHtLxvhgaF51uwMQkFsMha8J6Ono0R5yHUuA2OKpZJhTfvDG',
                  access_token_key='740758108507623425-qFMnPduxpTlzP2wOXHRNJpEhGHRqC3S',
                  access_token_secret='fLtxn1JrP4PZRZ3CKJJkZVG0ES3qjhDSR6NNpIGCRetqO')


t = api.GetUserTimeline(screen_name="filmwithjaysen", count=30)
tweets = [i.AsDict() for i in t]

for t in tweets:

        print(t['created_at'], t['text'])

