import praw
import os
import config



def bot_login():
    print ("Logging in..")
    try:
        r = praw.Reddit(user_agent=config.userAgent, 
                        client_id=config.cID, 
                        client_secret=config.cSC, 
                        username=config.userN, 
                        password=config.userP)
        print ("Logged in!")
    except:
        print ("Failed to log in!")
    return r