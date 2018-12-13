
# Imports
import twitter
import nltk
from operator import itemgetter
from nltk.corpus import wordnet as wn
import random

# Set up access credentials for the Twitter API
CONSUMER_KEY = 'tUx3gDmkwV2MIOteqhCPJ8nQL'
CONSUMER_SECRET = 'ceVcWk5sLfjz0np9sF2YlUoJiBT4cB4WmsqrSbi9EHChp3CA8O'
ACCESS_TOKEN = '838614187135942657-oKlOQzBPuX3jOyiwACrgbvRSxZAukMI'
ACCESS_TOKEN_SECRET = 'HBYIG9kvgCr2Tb2SkPFfma0bzkfI9OAimsH3FVcqdF17X'

# What do we want? Trump's tweets! 
# When do we want them? Never! 
username = "realDonaldTrump"
tweet_count = 5

# create an API instance for the Twitter API
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

# get Trump's 5 most recent tweets
tweets = api.GetUserTimeline(screen_name=username, count=tweet_count)

# choose a random tweet and extract the text
random_tweet = random.randint(0, (tweet_count-1))
tweet = tweets[random_tweet]
tweet = tweet.text

# Helper functions to write poems 
def tremendousPoem(status):
	'''
	Aha! A function that takes in a status and returns a TREMENDOUS poem.
	'''
	tremendousPoem = ""
	tokens = nltk.word_tokenize(status)
	partsOfSpeech = nltk.pos_tag(tokens)

	for ps in partsOfSpeech:
		# if it is a noun or a verb find a better one
		if ps[1] == "JJ" or ps[1] == "VB":
			synonyms = []
			antonyms = []

			for syn in wn.synsets(ps[0]):
				for l in syn.lemmas():
					synonyms.append(l.name())
					if l.antonyms():
						antonyms.append(l.antonyms()[0].name())
			if synonyms:
				tremendousPoem = tremendousPoem + " " + (random.choice(synonyms))
			if antonyms:
				tremendousPoem = tremendousPoem + " " + (random.choice(antonyms))

		elif ps[1] == "NN" or ps[1] == "NNP":
			tremendousPoem = tremendousPoem + " " + ps[0]

	tremendousPoem.capitalize()
	return tremendousPoem

def loudPoem(status):
	'''
	Returns a L O U D poem
	one that is in all caps and repeats the same word
	AGAIN AGAIN AGAIN
	'''
	loudPoem = ""
	tokens = nltk.word_tokenize(status)
	partsOfSpeech = nltk.pos_tag(tokens)

	nounList = []
	for ps in partsOfSpeech:
		if ps[1] == "JJ" or ps[1] == "NNP":
			nounList.append(ps[0])

	if nounList:
		entropyWord = random.choice(nounList)
		loudPoem = entropyWord

		while len(loudPoem) < (140 - len(entropyWord)):
			loudPoem = loudPoem + " " + entropyWord + " "

	else:
		loudPoem += "help"

	return loudPoem.upper()


def pandemoniumPoem(status):
	'''
	Returns some quality chaos, aka a poem that is shouted and jumbled 
	much as one might expect 
	from the current political situation.
	Dammit.
	'''
	pandemoniumPoem = ""
	tokens = nltk.word_tokenize(status)
	partsOfSpeech = nltk.pos_tag(tokens)

	nounList = []
	for ps in partsOfSpeech:
		if ps[1] == "JJ" or ps[1] == "NNP":
			nounList.append(ps[0])

	if nounList:
		entropyWord = random.choice(nounList)
		pandemoniumPoem = entropyWord

		while len(pandemoniumPoem) < (140 - len(entropyWord)):
			pandemoniumPoem = pandemoniumPoem + " " + entropyWord + " "
			entropyWord = random.choice(nounList)

	else:
		pandemoniumPoem += "help"

	return(pandemoniumPoem.upper())

def SADPoem(status):
	'''
	I think this one tries to reverse things 
	Negate them 
	etc 
	HAH 
	the futility 
	'''
	tokens = nltk.word_tokenize(status)
	SADtweet = ""

	for tok in tokens:
		antonyms = []
		for syn in wn.synsets(tok):
			for l in syn.lemmas():
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())

		if antonyms:
			SADRandomAntonym = random.choice(antonyms)
			SADtweet += SADRandomAntonym + " "
		else:
			SADtweet += tok + " "

	SADtweet = SADtweet[:140]
	return(SADtweet)

def beansPoem(status):
	'''
	Mood.
	'''
	status = "" # erase that shit purely for catharsis 
	beansPoem = "I'm beans."
	return(beansPoem)

# Randomly select one of the functions to generate a poem
# to ensure maximum chaos
function_array = [loudPoem(tweet), tremendousPoem(
	tweet), pandemoniumPoem(tweet), SADPoem(tweet), beansPoem(tweet)]
random_function_int = random.randint(0, (len(function_array)-1))

# Post the updated poem to Twitter
api.PostUpdate(function_array[random_function_int])


