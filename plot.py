import matplotlib.pyplot as plt
import numpy as np

def plot_bar_graph(all_users, number_of_users):
	x_axis_obj = []
	y_axis_val = []

	s = [(k, all_users[k]) for k in sorted(all_users, key=all_users.get, reverse=True)]
	
	i = 0
	for k, v in s:
		if i >= number_of_users:
			break
		x_axis_obj.append(k)
		y_axis_val.append(v)
		i += 1

	plt.barh(np.arange(len(x_axis_obj)), y_axis_val, align='center', alpha=0.5)
	plt.yticks(np.arange(len(x_axis_obj)), x_axis_obj)
	plt.xlabel('Number of messages')
	plt.title('Number of messages received from friends')
	plt.tight_layout()
	plt.gca().invert_yaxis()
	plt.show()	
