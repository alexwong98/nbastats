from nvd3 import lineChart
from stats import * 


# def generate_line_graph(player, stat):
# 	if stat in player['career_log'].columns:
# 		career_stats = get_career_stats(player, stat)
# 		moving_avg = moving_mean(career_stats, n =82)

# 		chart = lineChart(name="lineChart", width = 1500)
# 		xdata= range(len(career_stats))
# 		ydata= career_stats


# 		extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
# 		kwargs1 = {
# 			"y": ydata,
# 			"x": xdata,
# 			"name": stat,
# 			"extra": extra_serie,
# 		}

# 		chart.add_serie(**kwargs1)

# 		ydata2 = moving_avg
# 		kwargs2 = {
# 			"y": ydata2,
# 			"x": xdata,
# 			"name": "moving mean",
# 		}
# 		chart.add_serie(**kwargs2)

# 		# axisLabel = 'axisLabel'
# 		# axisLabel = axisLabel.decode('utf-8')
# 		# xAxisLabel = 'asdf'
# 		# xAxisLabel = xAxisLabel.decode('utf-8')
# 		# chart.axislist['xAxis'][axisLabel] = xAxisLabel

# 		chart.buildcontent()	

# 		return str(chart.htmlcontent)

# 	else:
# 		return None


#players is a list, graph each players stats and moving average
def generate_line_graph(players, stat):
	chart = lineChart(name="lineChart", width = 1500)
	for player in players:

		if stat in player['career_log'].columns:
			career_stats = get_career_stats(player, stat)
			moving_avg = moving_mean(career_stats, n =82)

			xdata= range(len(career_stats))
			ydata= career_stats

			extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
			kwargs1 = {
				"y": ydata,
				"x": xdata,
				"name": player['name'] + stat,
				"extra": extra_serie,
			}

			chart.add_serie(**kwargs1)

			ydata2 = moving_avg
			kwargs2 = {
				"y": ydata2,
				"x": xdata,
				"name": player['name'] + "moving mean",
			}
			chart.add_serie(**kwargs2)

			# axisLabel = 'axisLabel'
			# axisLabel = axisLabel.decode('utf-8')
			# xAxisLabel = 'asdf'
			# xAxisLabel = xAxisLabel.decode('utf-8')
			# chart.axislist['xAxis'][axisLabel] = xAxisLabel

		else:
			pass


	chart.buildcontent()	

	return str(chart.htmlcontent)

# player = create_player("Kobe", "Bryant")
# asdf = str(generate_line_graph(player, "PTS"))
# print(type(asdf))
# output_file = open('./templates/stats.html', 'w')
# output_file.write(asdf)
# output_file.close()