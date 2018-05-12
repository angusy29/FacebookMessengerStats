#!/usr/bin/python3

import argparse
import json
import matplotlib
import operator
import os
from plot import plot_bar_graph 

def create_new_user(all_users, user, sender_name):
	if sender_name == user or sender_name == 'Facebook User':
		return

	if sender_name in all_users:
		all_users[sender_name] += 1
	else:
		all_users[sender_name] = 1 

def parse_file(all_users, user, file):
	with open(file) as f:
		for elem in json.load(f)['messages']:
			if 'sender_name' in elem:
				create_new_user(all_users, user, elem['sender_name'])
			else:
				create_new_user(all_users, user, 'unknown_sender')

def walk_folders(all_users, user, dir):
	for item in os.walk(dir):
		if 'message.json' in files:
			# item[0] is root, item[1] is dirs, item[2] are files
			parse_file(all_users, user, os.path.join(item[0], 'message.json'))

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--user', type=str, required=True, help='Your name on Facebook, this is used to filter out your messages')
	parser.add_argument('-d', '--directory', type=str, help='Top level directory <./messages/folders/message.json>')
	return parser.parse_args()
	
if __name__ == "__main__":
	params = get_args()

	all_users = {}

	walk_folders(all_users, params.user, params.directory)

	sorted_users = sorted(all_users.items(), key=operator.itemgetter(1))	
	print(sorted_users)
	plot_bar_graph(all_users, 10)
