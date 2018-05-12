#!/usr/bin/python3

import argparse
import ast
import io
import json
from nltk.corpus import stopwords
import operator
from plot import show_image
import os
import re
from string import punctuation
from wordcloud import WordCloud

stop_words = set(stopwords.words('english'))

def process_content(all_words, user, elem):
	if 'sender_name' in elem:
		if elem['sender_name'] == user:
			if 'content' in elem:
				for word in elem['content'].split():
					clean_word = word.lower().strip(punctuation)
					if clean_word not in stop_words:
						all_words[clean_word] = all_words.get(clean_word, 0) + 1

def parse_file(all_words, user, file):
	with io.open(file, 'r', encoding='utf8') as f:
		for elem in json.loads(f.read())['messages']:
			process_content(all_words, user, elem)


def walk_folders(all_words, user, dir):
	for item in os.walk(dir):
		# item[0] is root, item[1] is dirs, item[2] are files
		if 'message.json' in item[2]:
			parse_file(all_words, user, os.path.join(item[0], 'message.json'))

def get_args():
	parser = argparse.ArgumentParser(description='Generate word cloud of most frequently used words')
	parser.add_argument('-u', '--user', type=str, required=True, help='Name of user')
	parser.add_argument('-d', '--directory', type=str, help='Top level directory <./messages/folders/message.json>')
	return parser.parse_args()
	
if __name__ == "__main__":
	params = get_args()

	all_words = {}

	walk_folders(all_words, params.user, params.directory)

	sorted_words = sorted(all_words.items(), key=operator.itemgetter(1))	
	print(sorted_words)

	wc = WordCloud(width=1920, height=1080, max_words=300, background_color='white').generate_from_frequencies(all_words)
	show_image(wc)
