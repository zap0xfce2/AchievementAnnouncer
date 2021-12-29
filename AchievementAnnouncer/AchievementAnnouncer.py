#!/usr/bin/env python3
# Created by Zap0xfce2 on May 2020

from Retroachievements import RetroAchievements
from datetime import datetime, timedelta
import json
import tweepy

# Configs laden
TwitterAPIKeyFile = open("config/TwitterApi.key", "r")
TwitterAPIKey = TwitterAPIKeyFile.read()

TwitterAPISecretKeyFile = open("config/TwitterApiSecret.key", "r")
TwitterAPISecretKey = TwitterAPISecretKeyFile.read()

TwitterAccessTokenFile = open("config/TwitterAccess.token", "r")
TwitterAccessToken = TwitterAccessTokenFile.read()

TwitterAccessTokenSecretFile = open("config/TwitterAccessToken.secret", "r")
TwitterAccessTokenSecret = TwitterAccessTokenSecretFile.read()

RAUserFile = open("config/RetroAchievements.user", "r")
RAUser = RAUserFile.read()

RAAPIKeyFile = open("config/RetroAchievements.key", "r")
RAAPIKey = RAAPIKeyFile.read()

LongURLFile = open("config/Long.url", "r")
LongURL = LongURLFile.read()

ShortURLFile = open("config/Short.url", "r")
ShortURL = ShortURLFile.read()

# Twitter Anmeldung
TwitterAuth = tweepy.OAuthHandler(TwitterAPIKey, TwitterAPISecretKey)
TwitterAuth.set_access_token(TwitterAccessToken, TwitterAccessTokenSecret)
Twitter = tweepy.API(TwitterAuth)

# RetroAchievements Anmeldung
RA = RetroAchievements(RAUser, RAAPIKey)

# 0 = heute oder Zahl an Tagen zurück abfragen
DayShift = 0
ApiDate = datetime.strftime(datetime.now() - timedelta(DayShift), '%Y-%m-%d')
# print(ApiDate)
AchivementsOfTheDay = RA.GetAchievementsEarnedOnDay(RAUser, ApiDate)
JsonRaw = json.dumps(AchivementsOfTheDay, sort_keys=True, indent=4)
JsonList = json.loads(JsonRaw)
# print(JsonRaw)

# Nur Twittern wenn die Liste Werte enthält
if JsonList:
    TweetToFile = open("LastTweet.txt", "w")
    # Aktuellstes Achievement aus der Liste nehemen
    ConsoleName = JsonList[-1]["ConsoleName"]
    GameTitle = JsonList[-1]["GameTitle"]
    AchievementTitle = JsonList[-1]["Title"]
    Tweet = "Bei " + GameTitle + " auf dem " + ConsoleName + " habe ich heute unter anderem den Erfolg \"" + AchievementTitle + "\" erzielt =) " + LongURL + " #RetroGaming"

    if len(Tweet) >= 280:
        # Tweet kürzen
        ShortTweet = "Bei " + GameTitle + " (" + ConsoleName + ") habe ich heute unter anderem den Erfolg \"" + AchievementTitle + "\" erzielt =) " + ShortURL
        # print(len(ShortTweet))
        # print(ShortTweet)
        Line = TweetToFile.write("Zeitstempel: " + datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\nText: " + ShortTweet + "\n")
        Twitter.update_status(ShortTweet)
    else:
        # print(len(Tweet))
        # print(Tweet)
        Line = TweetToFile.write("Zeitstempel: " + datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\nText: " + Tweet + "\n")
        Twitter.update_status(Tweet)

    TweetToFile.close()
