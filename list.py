list = [10,20,30,40, 40, 30]

print(list[5]) 
#Give the 5th index of the list

print(list[0:2]) 
#Give 0th and 1st index here 2nd index will not be included

print(list[:2])
 #This is as same as the above code

print(list[2:len(list)]) 
#This will print from 2nd index to last index

print(list[2:])
#This is as same as above code

print(list[0:5:2])
#This will print from 0th index to 5th index(excluded) the each 2nd element i.e one after one

print(list[-1])
#This will give the last element of the list

list.sort() 
#sort function is used to sort the listed items (if they are of same type)
print(list)

list.reverse()
#reverse function is used to reverse the positions of elements in the list
print(list)

list.append(90)
#append function is used to add a new element in the end of the list 
print(list)

list.insert(0,0)
#insert function is used to insert a new element in a particular position. In the above example it will add a 0 in the 0th index
print(list)

list.pop(0)
#pop function deletes an element using its index 
print(list)

list.remove(90)
#remove function deletes an element using it's value
print(list)
