import matplotlib.pyplot as plt
import numpy as np

def plot_bar_graph(all_users, number_of_users, title, xlabel):
	x = []
	y = []

	s = [(k, all_users[k]) for k in sorted(all_users, key=all_users.get, reverse=True)]
	
	i = 0
	for k, v in s:
		if i >= number_of_users:
			break
		x.append(k)
		y.append(v)
		i += 1

	print(x)
	print(y)
	fig, ax = plt.subplots(figsize=(13, 6))
	for i, v in enumerate(y):
		ax.text(v + 1.5, i, str(v), color='blue')

	ax.barh(np.arange(len(x)), y, align='center', color="blue")
	ax.set_yticks(np.arange(len(y)))
	ax.set_yticklabels(x, minor=False)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.gca().invert_yaxis()
	plt.show()


