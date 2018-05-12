#!/usr/bin/python3

import argparse
import json
import matplotlib
import operator
import os
from plot import plot_bar_graph 

def parse_file(users, user, friend, file):
	with open(file) as f:
		json_data = json.load(f)

		if 'title' not in json_data:
			return

		if friend not in json_data['title']:
			return

		for elem in json_data['messages']:
			if elem['sender_name'] == user:
				users[user] += 1
			else:
				users[friend] += 1

def walk_folders(users, user, friend, dir):
	for item in os.walk(dir):
		# item[0] is root, item[1] is dirs, item[2] are files
		if 'message.json' in item[2]:
			parse_file(users, user, friend, os.path.join(item[0], 'message.json'))

def get_args():
	parser = argparse.ArgumentParser(description='Find how many messages were sent between you and a friend')
	parser.add_argument('-u', '--user', type=str, required=True, help='Your name on Facebook')
	parser.add_argument('-f', '--friend', type=str, required=True, help='Your friend on Facebook')
	parser.add_argument('-d', '--directory', type=str, help='Top level directory <./messages/folders/message.json>')
	return parser.parse_args()
	
if __name__ == "__main__":
	params = get_args()

	users = { params.user: 0, params.friend: 0 }
	walk_folders(users, params.user, params.friend, params.directory)
	plot_bar_graph(users, 2)
