# Facebook Messenger Statistics

This repo consists of 3 runnable scripts:
* word_count.py
* pairs.py
* received.py

These scripts only work with JSON format.
Your Facebook data can be downloaded in Settings -> Your Facebook Information -> Download your information.

## Examples

* -u parameter is for your name
* -d is the top level directory you get after you unzip the Facebook zip. This should be called messages.

### Word cloud
```
python3 word_count.py -u "John Appleseed" -d messages
```
This will generate a word cloud of the user "John Appleseed" of the most frequently used words.

### Pairs
```
python3 pairs.py -u "Hideo Kojima" -f "Shigeru Miyamoto" -d messages
```
Plots a bar graph of the number of messages sent between you and your friend.

### Received
```
python3 received.py -d messages -u "Barack Obama" -t 10
```
Plots a bar graph of the number of messages which the top (-t) number of friends sent to me.

## Requirements
* Python 3
* nltk
* wordcloud
