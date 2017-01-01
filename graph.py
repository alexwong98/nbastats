from nvd3 import lineChart
from nbastats import *

pid = get_player_ID("Kobe", "Bryant");
kobeGameLog = render_player_game_log(pid, '2010-11')
points = get_season_stat(kobeGameLog, 'PTS')


chart = lineChart(name="lineChart")
xdata=range(82)
ydata= points

extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
kwargs1 = {
	"y": ydata,
	"x": xdata,
	"name": "sine",
	"extra": extra_serie,
}

chart.add_serie(**kwargs2)
chart.buildhtml()	
# print(chart.htmlcontent)
output_file = open('test_nvd3.html', 'w')
output_file.write(chart.htmlcontent)
output_file.close()
