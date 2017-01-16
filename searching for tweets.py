import twitter
import json
CONSUMER_KEY='6DH6eDvGWnLnnRfL10y3Lb6hM'
CONSUMER_SECRET='CI8Jtn2JR56I0VpW6DqCJwYd8k0H0AjmdugM4N69Ijy4qub4KH'
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''
auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api=twitter.Twitter(auth=auth)

q=["gym","swimming"]

count=100

search_results=twitter_api.search.tweets(q=q,count=count)

statuses=search_results['statuses']

for _ in range(5):
    print "Length of statuses",len(statuses)
    try:
        next_results=search_results['search_metadata']['next_results']
    except KeyError,e:
        break

    kwargs=dict([kv.split('=') for kv in next_results[1:].split("&")])

    search_results=twitter_api.search.tweets(**kwargs)
    statuses+=search_results['statuses']

print json.dumps(statuses[0],indent=1)
