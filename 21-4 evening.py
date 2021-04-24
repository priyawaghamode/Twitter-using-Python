#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


pip install tweepy


# In[3]:



import tweepy

def main():
    twitter_auth_keys = {
        "consumer_key" : "XhZMud6TjJS9BS7nLu9vnCcnE",
        "consumer_secret" : "fkOAHHkHgcuh022ttu1rBQltL35RT863ibV4qVn6BtDIQGIOqX",
        "access_token" : "1243119684913750017-2VpYgbMtSdg1UPRLM8ZYj1F8swGm2H",
        "access_token_secret" : "mJEhH9k2zs1cfaJFPbENGqhDy0n8q2eG3UEge18bEVTOf"
    }
    
    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )
    
    api = tweepy.API(auth)
    
    tweet = "Hello, this is my Tweet from my python Script"
    status = api.update_status(status=tweet)
    
main()


# In[ ]:



    


# In[ ]:





# In[ ]:




