import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("X4x4k70DB7LGbBCQ49yrLVdIu", "U3JpJIYNSJ0XA48qtk3zCxe0bWTcK7e2Dr3A62v8K6aXMVc8hb")
auth.set_access_token("1706198531743121408-EzJa4ON1JXmSaNg8y4MlMWePja7u24", "eMMXWAV22J6ScYC039ltSshkEpxrmR5g4ntxv4MuDPeXo")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Fetch tweets
tweets = api.search(q="Mdantsane crime", lang="en", count=10)

for tweet in tweets:
    print(f"{tweet.user.name} said {tweet.text}")
