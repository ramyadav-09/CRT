'''

Debugging Techniques:
1.Print()
2.Try and Except
3. Using of pdp

pdp -->Python Debugger
Purpose:
1.Pause the execution
2.inspect the variables value
3.to run 


pdp commands:
1.n--> to get output in next line
2.p variable --> to get the value of that variable
3.l-->list nearby code 
4.c-->continue the execution
5.s-->strat the function 
6.r-->to return from the function
7.h-->help 
8.q-->quit the execution
'''
'''try:
    a = int(input("Enter a"))
    print(10/a)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input") 
    '''
    
import pdb

def add(a,b):
    pdb.set_trace() #set a breakpoint pdp
    return a+b
a = int(input("Enter a"))
b = int(input("Enter b")) 
print(add(a,b))