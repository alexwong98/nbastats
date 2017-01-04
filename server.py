from flask import Flask, render_template, request
from graph import *
import pylibmc 

app = Flask(__name__)
mc = pylibmc.Client(["127.0.0.1"],
		behaviors={"tcp_nodelay": True, "ketama": True})

@app.route('/')
def home():
	return render_template("base.html")

@app.route('/', methods = ['POST'])
def search_player():
	name = request.form['player_name']
	stat = request.form['stat']
	name = name.title()
	full_name = name.split()
	pid = str(get_player_id(*full_name))
	
	if not (pid is None):
		if pid in mc:
			player = mc[pid]
		else:
			player = create_player(pid)
			mc[pid] = player
		stat_graph = generate_line_graph(player, stat)
		return render_template("stats_template.html", graph = stat_graph, player_name = name)
	else:
		return render_template("base.html", error = "Player does not exist.")

if __name__ == "__main__":
	app.run()