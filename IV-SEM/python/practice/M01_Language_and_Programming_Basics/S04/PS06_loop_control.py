'''
for i in range(1,11):
    if i%2 == 5:
        continue
    print(i,end = " ")



password retry system (max 3 attempte)
if password is correct show login successful
else ask for password 3 times.
once attempts exceed show account locked.
'''
p1 = "abc123"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("Login Successful")
        break
else:
    print("Account Locked")