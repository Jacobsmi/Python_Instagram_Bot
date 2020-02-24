from bot import Bot

def getHashtags():
    all_Hashtags = []
    more_Hashtags = True
    print("Please enter a hashtag you wish to search for\nWhen you are done press enter twice.\n")
    while(more_Hashtags):
        hashtag = input("Enter your hashtag here:")
        if(hashtag == ""):
            more_Hashtags = False
            return all_Hashtags
        else:
            all_Hashtags.append(hashtag)
            more_Hashtags = True

def main():
    hashtags = getHashtags()
    bot = Bot(hashtags)
    print("Running bot with hashtags {}".format(bot.hashtags))


if __name__ == "__main__":
    main()