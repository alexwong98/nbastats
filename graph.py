from nvd3 import lineChart
from stats import * 

kobe = create_player("Kobe", "Bryant")
kobe_career_stats = get_career_stats(kobe, 'PTS')


chart = lineChart(name="lineChart", width=2000)
xdata=range(len(kobe_career_stats))
ydata= kobe_career_stats

extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
kwargs1 = {
	"y": ydata,
	"x": xdata,
	"name": "sine",
	"extra": extra_serie,
}

chart.add_serie(**kwargs1)
chart.buildhtml()	
# print(chart.htmlcontent)
output_file = open('test_nvd3.html', 'w')
output_file.write(chart.htmlcontent)
output_file.close()
