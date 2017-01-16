import twitter
import json
from prettytable import PrettyTable
CONSUMER_KEY='6DH6eDvGWnLnnRfL10y3Lb6hM'
CONSUMER_SECRET='CI8Jtn2JR56I0VpW6DqCJwYd8k0H0AjmdugM4N69Ijy4qub4KH'
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''
auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api=twitter.Twitter(auth=auth)

q=raw_input('Enter your keywords: ')
#q=["gym","swimming"]

count=100

search_results=twitter_api.search.tweets(q=q,count=count)

statuses=search_results['statuses']

for _ in range(10):
    print "Length of statuses",len(statuses)
    try:
        next_results=search_results['search_metadata']['next_results']
    except KeyError,e:
        break

    kwargs=dict([kv.split('=') for kv in next_results[1:].split("&")])

    search_results=twitter_api.search.tweets(**kwargs)
    statuses+=search_results['statuses']

status_text=[status['text'] for status in statuses]


screen_names=[user_mention['screen_name'] for status in statuses
                                             for user_mention in status['entities']['user_mentions']]


hashtags=[hashtag['text'] for status in statuses
                              for hashtag in status['entities']['hashtags']]

for lable, data in (('Word',words),
                    ('Screen Name',screen_names),
                    ('Hashtag',hashtags)):
    pt=PrettyTable(field_names=[label,'Count']
print pt


