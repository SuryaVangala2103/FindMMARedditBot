import praw

#Write name of bot
reddit = praw.Reddit("Example bot name")

#fill in the subreddit where you would like the bot to run
#do not include the r/
subreddit = reddit.subreddit("example_subreddit")

while (True):
    for comment in subreddit.stream.comments(skip_existing=True):
        if "!FindMMABot" in comment.body:
            found_mma = False
            searchreddit_name = str(comment.body.replace("!FindMMABot", "").replace(" ", "").replace("r/", ""))
            searchreddit = reddit.subreddit(searchreddit_name)
            for submission in searchreddit.new(limit=100):
                if "MMA" in submission.title or "UFC" in submission.title:
                    comment.reply("www.reddit.com" + submission.permalink)
                    found_mma = True
                    break
            if not found_mma:
                comment.reply("I searched the 100 most recent posts in r/"
                              + searchreddit_name + " and found no MMA content")







