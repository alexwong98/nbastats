from nvd3 import lineChart
from stats import * 

def generate_line_graph(player, stat):
	if stat in player['career_log'].columns:
		career_stats = get_career_stats(player, stat)
		moving_avg = moving_mean(career_stats, n =82)

		chart = lineChart(name="lineChart", width = 1500, title="PLUS / MINUS")
		xdata=range(len(career_stats))
		ydata= career_stats

		extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
		kwargs1 = {
			"y": ydata,
			"x": xdata,
			"name": "sine",
			"extra": extra_serie,
		}

		chart.add_serie(**kwargs1)

		ydata2 = moving_avg
		kwargs2 = {
			"y": ydata2,
			"x": xdata,
			"name": "moving avg",
		}
		chart.add_serie(**kwargs2)

		chart.buildcontent()	

		return str(chart.htmlcontent)

		# with open('./templates/stats.html', 'r') as myfile:
		# 	stat_html = myfile.read()
		# stat_html = stat_html % {'graph' : chart.htmlcontent}
		# print(type(stat_html))
		# output_file = open('./templates/stats.html', 'w')
		# output_file.write(stat_html)
		# output_file.close()

	else:
		output_file = open('./templates/stats.html', 'w')
		output_file.write("{% extends \"base.html\" %}")
		output_file.write("error occured in stats")
		output_file.close()

# player = create_player("Kobe", "Bryant")
# asdf = str(generate_line_graph(player, "PTS"))
# print(type(asdf))
# output_file = open('./templates/stats.html', 'w')
# output_file.write(asdf)
# output_file.close()