"""
Sample Input : 1234
Sample Output : 4

Sample Input : 123456
Sample Output : 6

Sample Input : 45
Sample Output : 2
"""
"""
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

print(len(str(n)))
"""
"""
n = int(input())
temp = n
s = 0
while n > 0:
    s += (n % 10)
    n //= 10
print(s)

print(sum(map(int, str(temp))))
"""
"""
n = int(input())
even = odd = 0
while n > 0:
    if (n % 2) == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print(even,odd)
"""
"""
n = int(input())

while n > 9:
     n = sum(map(int, str(n)))
print(n)
"""

n = int(input())
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + (n % 10)
    n //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
    