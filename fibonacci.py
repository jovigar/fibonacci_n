first = 0
second = 1

print(first)
print(second)

for a in range (1,10):
    third = first+second 
    print(third)
    first, second = second,third

## Fibonacci generalizada a valor n valors anteriores a sumar
## n=2  0 1 1 2 3 5 8 13 21 44 65 
## n=3  0 1 1 2 4 7 13 24 44 81 149 274
## n=4  0 1 1 2 4 8 15 29 56 108 208 401
## n=5  0 1 1 2 4 8 16 

f=0
s=1
t=1

print(f)
print(s)
print(t)
for a in range (1,10):
    q=f+s+t
    print(q)
    f,s,t=s,t,q