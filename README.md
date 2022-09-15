# FindMMARedditBot

This is a reddit bot that will find the occurances of MMA content in a given subreddit

Steps:
1) Download repository
2) Go to https://www.reddit.com/prefs/apps/ while logged in to the account you want to use for the bot and make an application (button at very bottom of page), make sure that you select script 
3) Go to praw.ini and add the client id, client secret, username of bot account, and password of bot account (lines 31 - 34 of praw.ini). Fill in name of bot inside brackets on line 29 as well. 
4) Go to bot.py and add in the subreddit where you want to call the bot (line 8, do not include the r/) and the name of the bot (line 4)
5) Run bot.py via a terminal
6) Go to subreddit of choice and make a comment calling your bot and the name of a subreddit (for instance: !FindMMABot r/all)
7) Watch as bot finds isntances of MMA content in given subreddit 
8) When done with bot, close it in the terminal where you ran it
