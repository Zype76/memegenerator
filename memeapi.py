#!/usr/bin/python3
#By Paul Hansen
import json
from generator import gather
import os.path
import sys
import requests

#Argument format = (usr, passwd, meme, first line of text , second line of text, apiKey)
#Example: ./memeapi.py User Pass cat "I had fun once" "It was awful" "APIKEY"

result = gather(sys.argv[3])
urll = "http://version1.api.memegenerator.net//Instance_Create?username={0}&password={1}&languageCode=en&generatorID={2}&text0={3}&text1={4}t&apiKey={5}".format(sys.argv[1], sys.argv[2], result, sys.argv[4], sys.argv[5], sys.argv[6])

r = requests.get(urll)
print(r.json())
