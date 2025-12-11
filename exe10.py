print("------------------")
print("1")
print("------------------")
'''
* * _ * * 
* _ _ _ * 
_ _ _ _ _ 
* _ _ _ * 
* * _ * *
'''
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 3 or j == 3:
            print(" ", end=" ")
        else:
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            # elif i == 3 and j ==3:
            #     print(" ", end=" ")
            else:
                print(" ", end=" ")
    print()

# n = 5
# for i in range(1,n+1):
#     if i % 2 != 0:
#         for j in range(n+1-i-1):
#             print("*",end=" ")
#         for k in range(i):
#             print(" ",end=" ")
#         print()     
# for k in range(n,0,-1):
#     if k % 2 != 0:
#         for j in range(n-k+1):
#             print("*",end=' ')
#         for j in range(k-1):
#             print(' ', end=' ')
#         print()

print("------------------")
print("2")
print("------------------")
'''
_ _ * _ _ 
_ * * * _ 
* * * * * 
_ * * * _ 
_ _ * _ _ 
'''
n = 5
for i in range(1,n+1):
    if i % 2 != 0:
        for j in range(n+1-i-1):
            print(end=" ")
        for k in range(i):
            print("*", end=" ")
        print()     
for k in range(n,0,-1):
    if k % 2 != 0:
        for j in range(n-k+2):
            print(end=' ')
        for j in range(k-2):
            print('*', end=' ')
        print()

print("------------------")
print("3")
print("------------------")
'''
* 
* * 
* _ * 
* _ _ * 
* * * * * 
'''
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i == n or j == n or i == 1 or j == 1:
            print("*", end=" ")
        elif i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("------------------")
print("4")
print("------------------")
'''
* * * * * 
* _ _ _ * 
* _ _ _ * 
* _ _ _ * 
* * * * * 
'''
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == n or j == n or i == 1 or j == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("------------------")
print("5")
print("------------------")

'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''
n = 5
num = 1

for i in range(1,n+1):
    for j in range(1,i+1):
        print(num, end=" ")
        num += 1
    print()