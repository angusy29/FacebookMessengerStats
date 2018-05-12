import matplotlib.pyplot as plt
import numpy as np

def show_image(image):
	plt.imshow(image)
	plt.show()

def create_axis_arrays(all_users, number_of_users):
	x = []	# usernames
	y = []	# values

	s = [(k, all_users[k]) for k in sorted(all_users, key=all_users.get, reverse=True)]
	i = 0
	for k, v in s:
		if i >= number_of_users:
			break
		x.append(k)
		y.append(v)
		i += 1

	return x, y


def plot_bar_graph(all_users, number_of_users, title, xlabel):
	x, y = create_axis_arrays(all_users, number_of_users)

	_, ax = plt.subplots(figsize=(13, 6))
	for i, v in enumerate(y):
		ax.text(v + 1.5, i, str(v), color='blue')

	ax.barh(np.arange(len(x)), width=y, align='center', color="blue")
	ax.set_yticks(np.arange(len(x)))
	ax.set_yticklabels(x, minor=False)
	ax.invert_yaxis()

	plt.title(title)
	plt.xlabel(xlabel)
	plt.show()


