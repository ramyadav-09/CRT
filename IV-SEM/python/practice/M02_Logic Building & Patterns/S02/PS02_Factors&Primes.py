'''
Read a number from user and print all the factors of that number
input : 12
output : 1 2 3 4 6 12
'''
'''
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
print(n)
'''
'''
count no. of factors for a given number
'''
'''
n = int(input("Enter a number: "))
count = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        count += 1  
''' 
'''
check if a number is prime or not
'''
'''print("prime" if count == 1 else "not prime")'''
'''
print all the numbers in a given range
'''
'''
start = int(input(""))
end = int(input(" "))
if start ==1:
    start - 2
for n in range(start, end + 1):
    count = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    if count == 0:
        print(n, end=' ')
'''
'''
Factorial of a number
input : 5
output : 120
'''
'''num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)'''

'''GCD of two numbers'''
