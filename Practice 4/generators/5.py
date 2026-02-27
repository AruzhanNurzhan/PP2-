#Implement a generator that returns all numbers from (n) down to 0.

def ytr(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
for x in ytr(n):
    print(x,end=" ")
