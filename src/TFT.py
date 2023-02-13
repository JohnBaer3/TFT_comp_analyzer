# from riotwatcher import TftWatcher
# import pandas as pd
# import plotly.graph_objects as go
# import numpy as np

# api_key = 'RGAPI-6b376702-68aa-435c-954c-f12c37efee08'
# watcher = TftWatcher(api_key)
# my_region = 'na1'
# summoner_name = 'BardMidGG'

# me = watcher.summoner.by_name(my_region, 'LuxannaIRL')

# for key in me:
#     print(key, ':', me[key])


from riotwatcher import TftWatcher
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import json

api_key = 'RGAPI-6b376702-68aa-435c-954c-f12c37efee08'
watcher = TftWatcher(api_key)
my_region = 'na1'
summoner_name = 'BardMidGG'

me = watcher.summoner.by_name(my_region, summoner_name)

matches_ids = watcher.match.by_puuid(my_region, me['puuid'], count=1)

print(me['puuid'])

# how can I get the different time periods in a match... here? 

matches = [watcher.match.by_id(my_region, item) for item in matches_ids]

for match in matches:
	my_match_data = match #['info']#['participants'][match['metadata']['participants'].index(me['puuid'])]
	# my_match_data.keys()


	# print(my_match_data)

	json_string = json.dumps(my_match_data)
	# print(json_string)

	# with open('json_data.json', 'w') as outfile:
	# 	outfile.write(json_string)








































