import goldsberry as gb
from nba_py import player
from nba_py.player import get_player
from nba_py. player import PlayerNotFoundException
import pandas as pd 
import numpy as np


def get_career_stats(player, stat):
	if stat in player.career_log.columns:
		return player.career_log[stat].tolist()
	else:
		print("stat doesn't exist")
		return None 

def create_player(first, last):
	try:
		player = get_player(first, last)
		player.id = player.values[0]
	except PlayerNotFoundException:
		print (first + " " + last + " doesnt exist...")
		return None 

	demo = gb.player.demographics(player.id)
	demo = pd.DataFrame(demo.player_info())
	player.draft_year = format_year(demo['DRAFT_YEAR'].iloc[0])
	player.latest_year = format_year(demo['TO_YEAR'].iloc[0])
	player.name = str(demo['DISPLAY_LAST_COMMA_FIRST'].iloc[0])

	player_game_log = gb.player.game_logs(player.id)
	player.career_log = list()
	for year in range(int(player.draft_year[:4]),int(player.latest_year[:4])):
		player_game_log.get_new_data(Season = format_year(year))
		player_season_game_log = pd.DataFrame(player_game_log.logs())
		if not player_season_game_log.empty:
			player.career_log.append(player_season_game_log)

	player.career_log = pd.concat(player.career_log)
	
	return player

#returns their passing stats in a list ever since
#first player's first season 
#not usable due to sporadically unavailable data 
def get_recieving_stats(receiver, passer):
	fg_pct = dict()
	received = gb.player.passing_dashboard(receiver.id)
	for year in range(int(receiver.draft_year[:4]),int(receiver.latest_year[:4])):
		if int(passer.draft_year[:4]) <= year <= int(passer.latest_year[:4]):
			received.get_new_data(Season = format_year(year))
			received_df = pd.DataFrame(received.passes_received())
			if not received_df.empty:
				print received_df[received_df['PASS_TEAMMATE_PLAYER_ID'] == passer.id].loc[:,'FG_PCT']
	

#year is a string, a normal year ie 1998
#we want to convert to form that api accepts
#i.e. 1998-99
def format_year(first_half_of_season_year):
	second_half_of_season_year = str(int(first_half_of_season_year) + 1)[-2:]
	return str(first_half_of_season_year) + '-' + second_half_of_season_year


def next_season(formatted_season):
	return format_year(int(formatted_season[:4]) + 1)

def moving_mean(a, n = 25):
	ret = np.cumsum(a, dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return np.concatenate((np.zeros(n-1),ret[n - 1:] / n)) 
	



