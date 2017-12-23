#!/usr/bin/python3

#To pull the correct image for each meme

def gather(meme):
    if meme == "cat":
        generator = "1771888"
    elif meme == "brian":
        generator = "740857"
    elif meme == "futurama":
        generator = "84688"
    elif meme == "wonka":
        generator == "2729805"
    else:
        print("Im broken")
    return generator

