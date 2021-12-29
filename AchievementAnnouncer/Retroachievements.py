#!/usr/bin/env python3

import requests
import re
import json
import time


class RetroAchievements():
    def __init__(self, user, api_key):
        self.API_URL = 'https://retroachievements.org/API/'
        self.ra_user = user
        self.ra_api_key = api_key

    def auth_qs(self):
        return "?z=" + self.ra_user + "&y=" + self.ra_api_key

    def get_request(self, target, params=''):
        aq = self.auth_qs()
        url = self.API_URL + target + aq + '&' + params
        ret = requests.get(url).text
        j = json.loads(ret)
        return j

    def GetTopTenUsers(self):
        return self.get_request('API_GetTopTenUsers.php')

    def GetGameInfo(self, game_id):
        return self.get_request('API_GetGame.php', f'i={game_id}')

    def GetGameInfoExtended(self, game_id):
        return self.get_request('API_GetGameExtended.php', f'i={game_id}')

    def GetConsoleIDs(self):
        return self.get_request('API_GetConsoleIDs.php')

    def GetGameList(self, consoleid):
        return self.get_request('API_GetGameList.php', f'i={consoleid}')

    def GetFeedOf(self, user, count=1, offset=0):
        return self.get_request('API_GetFeed.php', f'u={user}&c={count}&o={offset}')

    def GetUserRankAndScore(self, user):
        return self.get_request('API_GetUserRankAndScore.php', f'u={user}')

    def GetUserProgress(self, user, gameidcsv):
        gameidcsv = re.sub(r'/\s+/', '', gameidcsv)
        return self.get_request('API_GetUserProgress.php', f'u={user}&i={gameidcsv}')

    def GetUserRecentlyPlayedGames(self, user, count=1, offset=0):
        return self.get_request('API_GetUserRecentlyPlayedGames.php', f'u={user}&c={count}&o={offset}')

    def GetUserSummary(self, user, numRecentGames):
        return self.get_request('API_GetUserSummary.php', f'u={user}&g={numRecentGames}&a=5')

    def GetGameInfoAndUserProgress(self, user, game_id):
        return self.get_request('API_GetGameInfoAndUserProgress.php', f'u={user}&g={game_id}')

    def GetAchievementsEarnedOnDay(self, user, dateInput):
        return self.get_request('API_GetAchievementsEarnedOnDay.php', f'u={user}&d={dateInput}')

    @classmethod
    def strtotime(cls, string, format_string="%Y-%m-%d %H:%M:%S"):
        tuple = time.strptime(string, format_string)
        return int(time.mktime(tuple))

    def GetAchievementsEarnedBetween(self, user, date_start, date_end):
        dateFrom = self.strtotime(date_start)
        dateTo = self.strtotime(date_end)
        return self.get_request('API_GetAchievementsEarnedBetween.php', f'u={user}&f={dateFrom}&t={dateTo}')
