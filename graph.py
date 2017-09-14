from nvd3 import lineChart
from stats import * 

#players is a list, graph each players stats and moving average
def generate_line_graph(players, stat):
  chart = lineChart(name="lineChart", width = 1500)
  for player in players:

    if stat in player['career_log'].columns:
      career_stats = get_career_stats(player, stat)
      moving_avg = moving_mean(career_stats, n = 25)

      xdata= range(len(career_stats))
      ydata= career_stats

      extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
      kwargs1 = {
        "y": ydata,
        "x": xdata,
        "name": player['name'] + ": " + stat,
        "extra": extra_serie,
        "disabled": True,
      }

      chart.add_serie(**kwargs1)

      ydata2 = moving_avg
      kwargs2 = {
        "y": ydata2,
        "x": xdata,
        "name": player['name'] +  ": " + "moving mean",
      }
      chart.add_serie(**kwargs2)
    else:
      pass


  chart.buildcontent()  

  return str(chart.htmlcontent)