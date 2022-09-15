# FindMMARedditBot

This is a reddit bot that will find the occurances of MMA content in a given subreddit

Steps:
1) Download repository
2) Go to https://www.reddit.com/prefs/apps/ while logged in to the account you want to use for the bot and make an application (button at very bottom of page), make sure that you select script. Use http://127.0.0.1 as redirect uri. Everything else can be blank. Add a description if you want. 
3) Go to praw.ini and fill in name of bot inside brackets on line 29. Add the client id, client secret, username of bot account, and password of bot account (lines 31 - 34 of praw.ini) as well
4) Go to bot.py and add the name of the bot (line 4) and the subreddit where you want to call the bot (line 8, do not include the r/) 
5) Run bot.py via a terminal
6) Go to subreddit of choice and make a comment calling your bot and the name of a subreddit (for instance: !FindMMABot r/all)
7) Watch as bot finds isntances of MMA content in given subreddit 
8) When done with bot, close it in the terminal where you ran it. The program will run infinitely unless you manually close it. 

Note: 
Please ignore the gitlink folder DogBreedCNN. The VCS system on my IDE was having problems. This should be an empty folder and is not relevant to this bot. 
