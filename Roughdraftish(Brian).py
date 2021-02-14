import sys,tweepy

# authentication Function

def twitter_auth():
	try: 
            consumer_key = 'enter yours xxxx'
	    consumer_seceret = 'enter yours xxxx'
	    access_token = 'enter yours xxxx'
	    access_secret = 'enter yours xxxx'

		
# If we can use the slack = Slacker('xoxb-1641899325365-1746817157600-fQUAOEfNFdlWICwpdSWYEvrD')
# A CSV file to not have to edit the source code itself, dff = pd.read_csv("twitter.csv")
	except KeyError:
		sys.stderr.write("TWITTER_* environment variable not set\n")
		sys.exit(1)
	auth = tweepy.OAuthHandler(consumer_key, consumer_seceret)
	auth.set_access_token(access_token, access_secret)
	     return auth

get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_reate_Limit=True)
    return client

    # This is use to enter a twitter users info, and if spits out all there tweets, got this from an article


if _name_ == '__main__':
	user = input ("Enter username: ")
	client = get_twitter_client()
	for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(n): #n = number of tweets
	   print(status.text)
