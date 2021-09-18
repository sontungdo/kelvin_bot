import praw

#Enter your correct Reddit information into the variable below

userAgent = 'kelvin_bot'
cID = '02pCvT8Biad-cFVL0ZENXg'
cSC= 'nF2phCM98blw7sQfkqkxrQCo3i7XLA'
userN = 'kelvin_bot'
userP ='botganktem20gg'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('test') #any subreddit you want to monitor

bot_phrase = 'Auto comment for testing. Please ignore me' #phrase that the bot replies with

keywords = {'test', 'testing'} #makes a set of keywords to find in subreddits

for submission in subreddit.hot(limit=5): #this views the top 10 posts in that subbreddit
    # ignore archieved posts
    if (submission.archived == True):
        continue
    n_title = submission.title.lower() #makes the post title lowercase so we can compare our keywords with it.
    for i in keywords: #goes through our keywords
        if i in n_title: #if one of our keywords matches a title in the top 10 of the subreddit
            numFound = numFound + 1
            print('Bot replying to: ') #replies and outputs to the command line
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)   
            print("Score: ", submission.score)
            print("---------------------------------")
            print('Bot saying: ', bot_phrase)
            print()
            submission.reply(bot_phrase)
            break #do NOT comment more than once per post

if numFound == 0:

    print()

    print("Sorry, didn't find any posts with those keywords, try again!")