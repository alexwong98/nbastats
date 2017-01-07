from flask import Flask, render_template, request
from graph import *
import pylibmc 
from werkzeug.contrib.cache import MemcachedCache

application = Flask(__name__)

cache = MemcachedCache(['127.0.0.1:11211'])

@application.route('/')
def home():
	return render_template("stats.html", stat = "PTS")

@application.route('/', methods = ['POST'])
def search_player():
	stat = request.form['stat']
	names = request.form['player_names']
	names_split = names.split(", ")

	players = list()
	for name in names_split:
		name = name.title()
		full_name = name.split()
		pid = str(get_player_id(*full_name))
	
		if not (pid is None):
			players.append(get_player_from_cache(pid))
		else:
			return render_template("stats.html", 
				error = "Player does not exist.")

	stat_graph = generate_line_graph(players, stat)
	return render_template("stats.html", graph = stat_graph, 
			player_names = names, stat = stat)
	
def get_player_from_cache(pid):
    player = cache.get(pid)
    if player is None:
        player = create_player(pid)
        cache.set(pid, player, timeout = 5 * 60)
    return player

if __name__ == "__main__":
	application.run(host='0.0.0.0')



