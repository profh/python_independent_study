# Chapter:		11
# Exercise:		5
# Start:		06:36:01 PM 07/06/2007
# End:			06:44:26 PM 07/06/2007
# Rating:		2
# Note:			Shows students how the functions work

def Lcount(myList, x):
	count = 0
	for s in myList:
		if s == x:
			count = count + 1
	return count
def Lisin(myList, x):
	for s in myList:
		if s == x:
			return True
	return False
def Lindex(myList, x):
	count = 0
	for s in myList:
		if s == x:
			return count
		count = count + 1
	return -1
def Lreverse(myList):
	newl = []
	for s in range(0, len(myList)):
		newl.append(myList.pop())
	return newl
def Lsort(myList):
	swap_test = False
	for i in range ( 0, len ( myList ) - 1 ):
		for j in range ( 0, len ( myList ) - i - 1 ):
			if myList[j] > myList[j + 1] :
				myList[j], myList[j + 1] = myList[j + 1], myList[j]
				swap_test = True
			if swap_test == False:
				break	
	return myList

def main():
	list = ["abc", "123", "test", "Ari", "Rubinstein", "123"]
	print list
	print Lcount(list, "123")
	print Lisin(list, "Ari")
	print Lindex(list, "Ari")
	print Lsort(list)
	print Lreverse(list)
	

main()
