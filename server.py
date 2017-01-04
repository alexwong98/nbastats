from flask import Flask, render_template, request
from graph import *
import pylibmc 

app = Flask(__name__)
mc = pylibmc.Client(["127.0.0.1"],
		behaviors={"tcp_nodelay": True, "ketama": True})

@app.route('/')
def home():
	return render_template("stats_template.html", stat = "PTS")

@app.route('/', methods = ['POST'])
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
			if pid in mc:
				player = mc[pid]
				players.append(player)
			else:
				player = create_player(pid)
				mc[pid] = player
				players.append(player)
		else:
			return render_template("stats_template.html", 
				error = "Player does not exist.")

	stat_graph = generate_line_graph(players, stat)
	return render_template("stats_template.html", graph = stat_graph, 
			player_names = names, stat = stat)
	
if __name__ == "__main__":
	app.run()