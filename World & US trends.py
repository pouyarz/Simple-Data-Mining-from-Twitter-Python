import twitter
CONSUMER_KEY='6DH6eDvGWnLnnRfL10y3Lb6hM'
CONSUMER_SECRET='CI8Jtn2JR56I0VpW6DqCJwYd8k0H0AjmdugM4N69Ijy4qub4KH'
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''
auth=twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api=twitter.Twitter(auth=auth)

WORLD_WOE_ID=1
US_WOE_ID=23424977

world_trends=twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends=twitter_api.trends.place(_id=US_WOE_ID)

import json

print json.dumps(world_trends,indent=1)
print
print json.dumps(us_trends, indent=1)
