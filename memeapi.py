#!/usr/bin/python3
#To showcase my python skills
#By Paul Hansen

import json
#import requests

apiKey="redacted"
languageCode = "en"
usr = "redacted"
passwd = "redacted"

def gather():
    meme = input("What image:") 
    print(meme)
    if meme == "1":
        generator = "1771888"
    elif meme == 2:
        generator = "740857"
    else:
        print("Im broken")
    return generator

fltext = input("First text line?")
sltext = input("Second line of text?")

result = gather()
print(result)
print("http://version1.api.memegenerator.net//Instance_Create?username={0}&password={1}&languageCode=en&generatorID={2}&text0={3}&text1={4}t&apiKey={5}".format(usr, passwd, result, fltext, sltext, apiKey))
