import praw
import bot_login
import time




def comment_post(r):
    """
    Function to comment to certain posts based on keyword
    @param r: Reddit instance, taken from bot_login function
    """
    numFound = 0 # number of posts to cmt
    for submission in r.hot(limit = 10): #this views the top 10 posts in that subbreddit
        # ignore archieved posts
        if (submission.archived == True):
            continue
        n_title = submission.title.lower() #makes the post title lowercase so we can compare our keywords with it.
        for i in keywords: #goes through our keywords
            if i in n_title: #if one of our keywords matches a title in the top 10 of the subreddit
                numFound += 1
                print('Bot replying to: ') #replies and outputs to the command line
                print("Title: ", submission.title)
                print("Text: ", submission.selftext)   
                print("Score: ", submission.score)
                print("---------------------------------")
                print('Bot saying: ', bot_phrase)
                print()
                submission.reply(bot_phrase)
                time.sleep(15)
                break #do NOT comment more than once per post
    if numFound == 0:
        print()
        print("Sorry, didn't find any posts with those keywords, try again!")

def reply_comment(r):
    """
    Function to reply to comments from a subreddit
    @param r: Reddit instance, taken from bot_login function
    """
    for comment in subreddit.stream.comments(skip_existing=True):
        if (comment.archived == True): # skip archived posts
            continue


r = bot_login.bot_login()
subreddit = r.subreddit('test') #any subreddit you want to monitor
bot_phrase = 'Auto comment for testing. Please ignore me' #phrase that the bot replies with
keywords = {'test', 'testing'} #makes a set of keywords to find in subreddits





