import math



tempList = []

def my_swap(list, i, j):
	#Implement swap.
	indexR = i
	tempR = 0
	sameNumber = 0
	#print(list)
	#print(len(list))
	if(indexR >= len(list)): 
		return
	for i in range(len(list)):
		if(i == len(list) - 1):
			break
		tempR = list[i]
		list[i] = list[i+1]
		list[i+1] = tempR
		if(list[i] == list[i+1]):
			sameNumber += 1
	tempList = list
	indexR += 1
	print(tempList)
	if(sameNumber == len(list)-1):
		return
	my_swap(tempList, indexR, len(tempList))
	#print(list)
	
steps = -1
methods = [[5,4,1],[-1,4,1],[-1,-1,1]] #Prepare for the next deep learning and AI
totalCount = 0;
steps = int(input("Steps that you can jump? "))
n = steps #steps
index = 0
resultList = []
tempList = []
for i in range(0, len(methods)):
	result = []
	temp = n
	for j in range(0, temp):
		#Add more methods to robot
		if(temp / methods[i][0] >= 1 and temp >= methods[i][0]):
			result.append('5')
			temp -= 5
		if(temp / methods[i][1] >= 1 and temp >= methods[i][1]):
			result.append('4')
			temp -= 4
		if(temp / methods[i][2] >= 1 and temp >= methods[i][2]):
			result.append('1')
			temp -= 1
	resultList.append(result)

cleanList = []
tempList = resultList
for elem in resultList:
	if elem not in cleanList:
		cleanList.append(elem)
print(cleanList)

for list in cleanList:
	my_swap(list, 0, len(list))
	

#Remove duplicated elements
#my_swap(cleanList)





#Recuration.

#Recurstion and memoization.

#Divide and Conquer and Matrix.



