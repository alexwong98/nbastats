from flask import Flask, render_template
from graph import *


app = Flask(__name__)

@app.route('/')
def hello():
	player = create_player("Kobe", "Bryant")
	generate_line_graph(player, "PTS")
	return render_template("stats.html")

if __name__ == "__main__":
	app.run()