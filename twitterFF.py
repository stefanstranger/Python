#!/usr/bin/env python

#
#Auto #FF Follow Friday Twitter Python script
#randomly picking friends (people you follow on Twitter)

# Author
#  - Stefan Stranger (@sstranger)
#  - http://www.stranger.nl
#
# Usage
#
# Install the Twython Python Wrapper from:
# https://github.com/ryanmcgrath/twython
# Get your keys from https://dev.twitter.com/
# Change the api key values marked ##### below with the twitter keys
# Schedule twitterFF.py using crontab or another task scheduler to run every Friday.

import time
import random
from twython import Twython
CONSUMER_KEY = '####'
CONSUMER_SECRET = '####'
ACCESS_KEY = '####'
ACCESS_SECRET = '####'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


friends = api.get_friends_ids(screen_name="yourtwitterhandle")
new_list = []
for x in friends["ids"]:
	new_list.append(x)


#print random id 6 times
ff = ''
for y in range(1,7):
	id_position = random.randint(0, len(new_list) -1)
	userid = new_list[id_position]
	data = api.show_user(user_id=userid)
	following = data["screen_name"]
	ff = ff + ' ' + '@' + following

api.update_status(status='#FF ' + ff)
