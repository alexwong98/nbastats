import os
from flask import Flask, render_template, request
# from graph import *
from stats import *
import pylibmc 
from werkzeug.contrib.cache import MemcachedCache
import player_kmeans
import numpy as np
import pandas as pd 
import json

templateDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app/backend/templates')
staticDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app/backend/static')

app = Flask(
    __name__,
    template_folder = templateDirectory,
    static_folder = staticDirectory
)

cache = MemcachedCache(['127.0.0.1:11211'])
players_df = player_kmeans.cluster()

@app.route('/')
def home():
    return render_template('stats.html', stat = 'PTS')


@app.route('/', methods = ['POST'])
def search_player():
  stat = request.form['stat']
  names = request.form['player_names']
  names_split = names.split(", ")

  players = []
  for name in names_split:
    name = name.title()
    full_name = name.split()
    pid = str(get_player_id(*full_name))
  
    if not (pid is None):
      players.append(get_player_from_cache(pid))
    else:
      return render_template("stats.html", 
        error = "Player does not exist.")

  similar_players = []
  player_type = ''

  if len(players) == 1 and len(names_split) == 1:
    player_type, similar_players = player_kmeans.get_similar_players(players_df, names_split[0])

  similar_players = map(lambda p: p[1]['Player'], similar_players)
  # stat_graph = generate_line_graph(players, stat)

  print json.dumps(get_data(players, stat))
  return render_template("stats.html", 
    player_names = names, 
    stat = stat, 
    data = json.dumps(get_data(players, stat)),
    similar_players = similar_players,
    player_type = player_type
  )
  
def get_player_from_cache(pid):
  player = cache.get(pid)
  if player is None:
    player = create_player(pid)
    cache.set(pid, player, timeout = 5 * 60)
  return player

if __name__ == "__main__":
  app.run(host='0.0.0.0')