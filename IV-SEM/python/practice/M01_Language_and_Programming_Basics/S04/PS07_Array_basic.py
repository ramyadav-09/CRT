'''
import array
arr = array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.append(12.45)
'''

li = [12,25.4,6+5j,]
print(li[::-1])
print(len(li))
li.append(100)
print(li)
li.insert(2,"World")
print(li) 

#read a number from the user and display no. of digits in that number 
input : 1234
output : 4