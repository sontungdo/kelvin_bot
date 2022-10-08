import praw
import bot_login
import time
import re
import convert


def comment_post(r, keywords, bot_phrase):
    """
    Function to comment to certain posts from a subreddit based on keyword
    @param r: SubReddit instance, taken from bot_login function
    @param keywords: array of strings to look for in a subreddit
    @param bot_phrase: string that bot will comment 
    """
    numFound = 0 # number of posts to cmt
    print("Searching for posts...")
    try:
        for submission in r.stream.submissions(skip_existing=True): #this views the top 10 posts in that subbreddit
            # ignore archieved posts
            if (submission.archived == True):
                continue
            n_title = submission.title.lower() #makes the post title lowercase so we can compare our keywords with it.
            for i in keywords: #goes through our keywords
                if i in n_title: #if one of our keywords matches a title in the top 10 of the subreddit
                    print("---------------------------------")
                    print('Bot replying to: ') #replies and outputs to the command line
                    print("Title: ", submission.title)
                    print("Text: ", submission.selftext)   
                    print("Score: ", submission.score)
                    print('Bot saying: ', bot_phrase)
                    print("---------------------------------")
                    print()
                    submission.reply(bot_phrase)
                    numFound += 1
                    time.sleep(15)
                    break #do NOT comment more than once per post
    except:
        print("Error")
    if numFound == 0:
        print()
        print("Sorry, didn't find any posts with those keywords, try again!")

def reply_comment(r, keywords, bot_phrase):
    """
    Function to comment to certain posts from a subreddit based on keyword
    @param r: SubReddit instance, taken from bot_login function
    @param keywords: array of strings to look for in a subreddit
    @param bot_phrase: string that bot will comment 
    """
    #numFound = 0 # number of posts to cmt
    print("Searching for comments...")
    try:
        for comment in r.stream.comments(skip_existing=False): # view stream of comments
            if (comment.archived == True): # skip archived comments
                continue
            n_comment = comment.body.lower() #makes the comment lowercase so we can compare our keywords with it.
            for i in keywords: #goes through our keywords
                if i in n_comment: #if one of our keywords matches a comment
                    print("---------------------------------")
                    print('Bot replying to:', comment.author) #replies and outputs to the command line
                    print("Comment: ", comment.body)   
                    print("Score: ", comment.score)
                    print('Bot saying: ', bot_phrase)
                    print("---------------------------------")
                    print()
                    #comment.reply(bot_phrase)
                    #numFound += 1
                    time.sleep(5)
                    break #do NOT reply more than once per comment
    except:
        print()
        print("Sorry, please try again!")

def reply_comment(r, pattern):
    """
    Function to comment to certain posts from a subreddit based on regex pattern
    @param r: SubReddit instance, taken from bot_login function
    @param pattern: regex pattern to match
    """
    print("Searching for comments...")
    try:
        for comment in r.stream.comments(skip_existing=False): # view stream of comments
            if (comment.archived == True): # skip archived comments
                continue
            n_comment = comment.body #makes the comment lowercase so we can compare our keywords with it.
            match = re.findall(pattern, n_comment)
            if (match):
                # convert temperature
                og_num = float(match[0][0]) # amount of original measurement
                og_unit = match[0][2].upper() # unit of original measurement
                convert_num = convert.convert(og_num, og_unit)
                kelvin_num = convert.to_kelvin(og_num, og_unit)
                if (og_unit == "F"):
                    convert_unit = "C"
                elif (og_unit == "C"):
                    convert_unit = "F"
                # construct bot reply
                bot_phrase = str(int(og_num)) + "°" + og_unit + " is equivalent to " +\
                    str(int(convert_num)) + "°" + convert_unit + ", which is " + str(int(kelvin_num)) \
                    + "K.\n---\n^(I'm a bot that converts temperature between two units humans "\
                    + "can understand, then convert it to Kelvin for bots to understand)"
            
                # Terminal message
                print("---------------------------------")
                print('Bot replying to:', comment.author) #replies and outputs to the command line
                print("Comment: ", comment.body)   
                print("Score: ", comment.score)
                print('Bot saying: ', bot_phrase)
                print("---------------------------------")
                print()
                comment.reply(bot_phrase)
                time.sleep(5)
                #break #do NOT reply more than once per comment
    except KeyboardInterrupt:
        print()
        print("Terminated")
        exit(0)

if __name__ == "__main__":
    r = bot_login.bot_login()
    subreddit = r.subreddit('all') #any subreddit you want to monitor
    keywords = {' c ', ' f '} #makes a set of keywords to find in subreddits

    # strict pattern search that only finds properly formatted temperature
    pattern = r'\s+([+-]?\d+(\.\d+)?)\s?°([CF])\s+' # can add ? after ° to broaden up the search
    
    kelvin_pros = "Kelvin is the best measurement for temperature. As it is an absolute temperature scale,"\
        " measurements in Kelvin can not only be compared to each other but can also be weighted"\
        " against each other in the form of a ratio. For example, you could say that 200K is twice"\
        " as hot as 100K, but neither 200°C or 200°F could be said to be twice as hot as 100°C or 100°F,"\
        " respectively.\nPlease PM me if I incorrectly understand the meanings of your comment"


    #comment_post(subreddit, keywords, bot_phrase)
    try:
        while True:
            reply_comment(subreddit, pattern)
    except KeyboardInterrupt:
        print('interrupted!')
        exit(0)




