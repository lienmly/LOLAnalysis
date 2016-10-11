URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',

    #/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',

    #/api/lol/{region}/v2.5/league/by-summoner/{summonerIds}
    'get_ranked_match': 'v{version}/league/by-summoner/{summonerid}',

    #/api/lol/{region}/v2.2/match/{matchId}?includeTimeline={timeline_bool}
    'match_data': 'v{version}/match/{matchid}?includeTimeline={timeline_bool}',

    #/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}
    'match_history': 'v{version}/matchlist/by-summoner/{summonerId}'
    }

API_VERSIONS = {
    'summoner': '1.4',
    'ranked_match': '2.5',
    'match': '2.2'
    }

REGIONS = {
    'north_america': 'na',
    }

MATCH_ID = {
    '1': '2141841204',
    '2': '2135064746',
    '3': '2098351997',
    }
