from selenium import webdriver
import random
import string
import argparse
#from selenium.webdriver.common.keys import Keys
#import getpass

class AutoSubmit:

	def __init__(self, driver='edge'):
		self.driver = connectToDriver(driver)

	def runSearches(self, wordList, numSearches=100):
		numSearches = int(numSearches)
		searchesCompleted = 0
		while searchesCompleted < numSearches:
			word = random.choice(wordList)
			self.driver.get(word)
			searchesCompleted += 1
		return 0

def createWordList(filename=None):
	if filename is None:
		wordList = generateRandomWordList()
	else:
		wordList = importWordList(filename)
	return wordList

def generateRandomWordList():
	wordList = []
	while len(wordList) < 100:
		wordList.append(generateWord())
	return wordList

def generateWord():
	word = ''
	while len(word) < 10:
		word += random.choice(string.letters)
	return word


def importWordList(filename):
	wordList = open(filename).read().splitlines()
	return wordList


def connectToDriver(selectedDriver):
	if selectedDriver == 'edge':
		return webdriver.Edge()
	return None


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Used to auto search bing for BingReward points")
	parser.add_argument('-d', '--driver', help="Driver to search with (edge, firefox, chrome)")
	parser.add_argument('-f', '--filename', help="Filename of desired word list")
	parser.add_argument('-n', '--numSearches', help="Number of searches to perform")
	args = parser.parse_args()

	wordList = createWordList(args.filename)

	if (args.driver):
		auto = AutoSubmit(args.driver)
	else:
		auto = AutoSubmit()

	print "Driver created."

	if (args.numSearches):
		auto.runSearches(wordList, args.numSearches)
	else:
		auto.runSearches(wordList)


	auto.driver.close()
	print "Searching complete."
