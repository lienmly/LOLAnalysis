#=========================================
# Lien Ly - main function call 
#=========================================
import getMatchAuto as a
from RiotAPI import RiotAPI

def main():
    # api = RiotAPI('314c9e1a-a062-40e0-acc4-c4ff55eefb2b')

    # r = api.get_summoner_by_name('lucas1432')
    # r = api.requestRankedData('62280492',str('314c9e1a-a062-40e0-acc4-c4ff55eefb2b'))
    # r = api.get_match_info('2141841204')
    # print(r)

    a.getGoldFrames()
    
if __name__ == "__main__":
    main()
