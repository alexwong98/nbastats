from flask import Flask, render_template, request
from graph import *


app = Flask(__name__)

@app.route('/')
def home():
	return render_template("base.html")

@app.route('/', methods = ['POST'])
def search_player():
	name = request.form['player_name']
	name = name.title()
	full_name = name.split()
	player = create_player(*full_name)
	# if not player == None:
	stat_graph = generate_line_graph(player, "PTS")
	return render_template("stats_template.html", graph = stat_graph)
	# else:
	# 	return render_template("base.html")

if __name__ == "__main__":
	app.run()