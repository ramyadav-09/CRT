'''li = [1,2,3,4,5]
output : [2,4,6,8,10]'''
'''li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i*2)
print(res)
print([i*2 for i in li])

#['a','b','c'] ==> "abc" 
li1 = ['a','b','c']
res = ""
for ch in li1:
    res += ch
print(res)
print("".join(li1))
'''
'''
Intermediate patterns
1. Pyramid
n = 4
Output:
    *
   * *
  * * *
 * * * *
'''
'''n = 4
for i in range(1,n+1):  
    print(" "*(n-i)+"* "*i)
'''
'''2. Inverted Pyramid:
n = 4
Output:
   * * * *
    * * *
     * *
      *
'''
'''n = 4
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
'''
'''3. Diamond:
n = 4
Output:
       *
      * *
     * * *
    * * * *
     * * *
      * *
       *
'''
n = 4
for i in range(1,n+1):  
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i) 

'''numbers pattern:
output:
      1
     1 2
    1 2 3
   1 2 3 4
'''
'''
n = 4
for i in range(1,n+1): 
    print(" "*(n-i)+" ".join(str(x) for x in range(1,i+1)))
'''
'''
print numbers
output:
      1
     2 2
    3 3 3
   4 4 4 4
'''
'''n = 4
for i in range(1,n+1): 
    print(" "*(n-i)+" ".join(str(i) for x in range(i)))
'''
'''alfhabet pattern:
output:
A
B C
D E F
G H I J
'''
n = 4
ch = 65
for i in range(1,n+1): 
    row = []
    for j in range(i):
        row.append(chr(ch))
        ch += 1
    print(" ".join(row))

'''

'''