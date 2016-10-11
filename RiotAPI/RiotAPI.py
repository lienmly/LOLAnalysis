import requests
import RiotContants as Consts

class RiotAPI(object):

    def __init__(self,api_key,region=Consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
                ),
            params=args
            )
        #print (response.url)
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
            )
        return self._request(api_url)

    def requestRankedData(self, ID, APIKey, region=Consts.REGIONS['north_america']):
        #URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
        api_url = Consts.URL['get_ranked_match'].format(
            version=Consts.API_VERSIONS['ranked_match'],
            summonerid=ID
            )
        print (api_url)
        #response = requests.get(URL)
        return self._request(api_url)

    def get_match_info(self, matchID, timeline_included=True):
        api_url = Consts.URL['match_data'].format(
            version=Consts.API_VERSIONS['match'],
            matchid=matchID,
            timeline_bool=timeline_included
            )
        return self._request(api_url)
    
    def get_match_history(self, summonerID):
        api_url = Consts.URL['match_history'].format(
            version=Consts.API_VERSIONS['match'],
            summonerId=summonerID
            )
        return self._request(api_url)
