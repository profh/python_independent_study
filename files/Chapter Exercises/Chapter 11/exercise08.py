# Chapter:		11
# Exercise:		8
# Start:		06:52:42 PM 07/06/2007
# End:			07:00:49 PM 07/06/2007
# Rating:		3
# Note:			Shows how to test if something is in a list, then add to it
def Lisin(myList, x):
	for s in myList:
		if s == x:
			return True
	return False

def removeDuplicates(list):
	wordlist = []
	for s in list:
		if not Lisin(wordlist, s):
			wordlist.append(s)
	
	return wordlist

def main():
	li = ["Ari", "Rubinstein", "Is", "The", "Coolest", "Person", "There", "Is", "In", "The", "Universe"]
	print li
	li = removeDuplicates(li)
	print li
main()
