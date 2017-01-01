import goldsberry as gb
from nba_py import player
from nba_py.player import get_player
from nba_py. player import PlayerNotFoundException
import pandas as pd 


def get_player_ID(first, last):
	try:
		player = get_player(first, last)
		return player.values[0]
	except PlayerNotFoundException:
		print (first + " " + last + " doesnt exist...")
		return None 

def render_player_game_log(pid, season):
	player_game_log = gb.player.game_logs(pid, Season = season)
	player_season_game_log = pd.DataFrame(player_game_log.logs())
	return player_season_game_log

def get_season_stat(game_log, stat):
	return game_log.loc[:,stat]; 

pid = get_player_ID("Kobe", "Bryant");
kobeGameLog = render_player_game_log(pid, '2010-11')
points = get_season_stat(kobeGameLog, 'AST')
print points



