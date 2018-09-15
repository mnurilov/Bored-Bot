#Imports 
import praw
import re
import random

#Initializing the reddit bot using a praw ini file
reddit = praw.Reddit('bot1')

#This is were you select your subreddit
#Currently no subreddit is selected feel free to enter any subreddit
subreddit = reddit.subreddit("")

#Bored bots recommendations for entertaining content
boredBot_responses = \
[
"https://www.youtube.com/watch?v=JbepN4dKLbU", #Thats a 10 video
"https://www.youtube.com/watch?v=NpYqFJxVuBc", #Kingdom Hearts Live Action
"https://www.youtube.com/watch?v=8YWl7tDGUPA", #Color Red
"https://www.youtube.com/watch?v=cuNhfSM-144", #Lady flipping
"https://www.youtube.com/watch?v=EWF8Nfm-LLk", #Five Gum
"https://www.youtube.com/watch?v=q-CmExEDY6c", #Stole a kiss
"https://www.youtube.com/watch?v=IIL5klObiQ4", #Half Life Wounded
"https://www.youtube.com/watch?v=FwT87jKjfUU", #Picture Frame
"https://www.youtube.com/watch?v=ZVboVv59fLQ", #Dog Helicopter
"https://www.youtube.com/watch?v=WNmCm4oyrkY", #What are you doing Computer
]

#This for loop repeats forever and always checks for comments
for comment in subreddit.stream.comments():
    print(comment.body)
    #This is the phrase that the bot searches for
    if re.search("I am bored", comment.body, re.IGNORECASE):
        #This is the response that reddit bot gives
        boredBot_reply = "Bored Bot recommends: " + random.choice(boredBot_responses)
        comment.reply(boredBot_reply)
        print(boredBot_reply)
            

