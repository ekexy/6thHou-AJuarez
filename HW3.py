#AJ
#6th hour
#HW3
#I got help from https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/

#Print Hello World
print("Hello World")
#Make a list containing 6 animals
animList = ["Dog","Cat","Fish","Rat","Wolf","Cheetah"]
#Insert another animal that isn't in the list
animList.insert(2,"Owl")
#Print animal added
print(animList[2])
#make another list containing 8 int random order
numList = [4,6,7,8,9,3,2,5]
#sort the list from highest to lowest
numList.sort(reverse=True)
#print the whole list out
print(numList)
#subtract the first number on the list from the last
diff = numList[0] - numList[7]
#print out the difference
print(diff)