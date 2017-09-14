import numpy as np
import pandas as pd 
import math
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import cluster, metrics
from heapq import nsmallest

def kmeans(reduced_data, n_clusters):
  kmeans = KMeans(n_clusters=n_clusters, random_state=42)
  kmeans = kmeans.fit(reduced_data)
  labels = kmeans.labels_
  centroids = kmeans.cluster_centers_
  inertia = kmeans.inertia_
  s_score = metrics.silhouette_score(reduced_data, kmeans.labels_, metric='euclidean')

  data_dictionary = {
    "labels": labels,
    "centroids": centroids,
    "inertia" : inertia,
    "silhouette_score": sil_score
  }

  return data_dictionary

def feature_importance(cluster_data, league_data):
  scaler = StandardScaler()
  scaled_data = scaler.fit_transform(cluster_data)

  pca = PCA(n_components=2)
  PCA_reduced_df = pca.fit(scaled_data).transform(scaled_data)

  features = pd.DataFrame(zip(cluster_data.columns, pca.components_[0], np.mean(cluster_data), np.mean(league_data)),
    columns=['Feature', 'Importance', 'Cluster Average', 'League Average']).sort_values('Importance', ascending=False).head(10)

  return features

def distance(tuple1, tuple2):
  return math.sqrt(math.pow((tuple2[0] - tuple1[0]),2) + math.pow((tuple2[1] - tuple1[1]),2))

def get_similar_players(players_df, player_name):
  player = players_df[players_df['Player'].str.lower() == player_name.lower()]

  if not player.empty:
    player = player.iloc[0]
    mask = (players_df['labels'] == player['labels']) & (players_df['Player'] != player['Player'])
    player_group = players_df[mask]  
    return player['labels'], nsmallest(10, player_group.iterrows(), key=lambda p: distance((player['X1'], player['X2']),(p[1]['X1'], p[1]['X2'])))
  else:
    return 'Unknown', []

def cluster():
  file_name = 'data/stats.csv'

  data = pd.read_csv(file_name)

  #clean data 
  data.drop(['Unnamed: 0', 'MP', '3PAr'], axis=1)
  data = data[data['G'] > 40]

  #data preprocessing
  x = data.drop(['Player', 'Pos', 'G', 'Player_ID', 'Status'], axis=1)
  y = data['Pos']

  scaler = StandardScaler()
  x_scaled = scaler.fit_transform(x)

  pca = PCA(n_components=2)
  pca.fit(x_scaled)

  X_pca = pca.transform(x_scaled)

  LDA = LinearDiscriminantAnalysis(n_components=2, shrinkage='auto', solver='eigen')
  LDA_reduced_df = LDA.fit(x_scaled,y).transform(x_scaled)


  kmeans_cluster = kmeans(LDA_reduced_df, 8)
  data['Cluster'] = kmeans_cluster['labels']
  y = kmeans_cluster['labels']
  df = pd.DataFrame({'X1':LDA_reduced_df[:,0],'X2':LDA_reduced_df[:,1], 'labels':y})

  player_list = list(data['Player'])
  status_list = list(data['Status'])
  playerid_list = list(data['Player_ID'])

  df['Player'] = player_list
  df['Status'] = status_list
  df['Player_ID'] = playerid_list
  df['labels'] = df['labels'].map({0: 'Defensive Centers',
    1: '3-and-D Wings',
    2: 'Scoring Wings',
    3: 'Versatile Forwards',
    4: 'Floor Generals',
    5: 'Shooting Wings',
    6: 'Combo Guards',
    7: 'Offensive Centers'})

  return df 