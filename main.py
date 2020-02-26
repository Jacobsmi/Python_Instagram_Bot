from bot import Bot

def main():
    bot = Bot('pythonbot59','Testing01867')
    bot.getHashtags()
    print("Running bot with hashtags {}".format(bot.hashtags))
    bot.login()


if __name__ == "__main__":
    main()