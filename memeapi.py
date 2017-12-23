#!/usr/bin/python3
#By Paul Hansen
import json
import sys
import requests
from generator import gather

#Argument format = (usr, passwd, meme, first line of text , second line of text, apiKey)
#Example: ./memeapi.py User Pass cat "I had fun once" "It was awful" "APIKEY"

urll = "http://version1.api.memegenerator.net//Instance_Create?username={0}&password={1}&languageCode=en&generatorID={2}&text0={3}&text1={4}&apiKey={5}".format(sys.argv[1], sys.argv[2], gather(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6])

r = requests.get(urll)
form = r.json()

print("Image link:", form['result']['instanceImageUrl'])
