print("---------FIBONACCI normal ---------------")
first = 0
second = 1

print(first)
print(second)

for a in range (1,10):
    third = first+second 
    print(third)
    first, second = second,third
print("----------------------------------")
## Fibonacci generalizada a valor n , 
#  n valores anteriores a sumar
## n=2  0 1 | 1 2 3 5 8 13 21 44 65 
## n=3  0 1 2 | 3 6 11 20 37 68 125 230 423
## n=4  0 1 2 3 | 6 12 23 44 85 164 316 609 1174
## n=5  0 1 2 3 4 | 10 20 39 76 149 294 578 1136 2233
## n=6  0 1 2 3 4 5 | 15 30 59 116 229 454 903 1791 3552


# valor n de entrada 
# n puede ser = 2, 3, 4, 5, 6, 7, 8, ...

 #array dinamico o lista de n numeros, esos son los que hay que sumar
print("---------FIBONACCI generalizado ---------------")

n = int(input('Enter the number sums (must be > 2): ')) 
listasuma =[]
for i in range (n):
    listasuma.append(i)

#cls
# print(listasuma)

for a in range (1,10):
     
    q=0 
    for x in listasuma:
          #print(x)
          q = q + x
         
          
    print(q)
    listasuma.pop(0)
    listasuma.append(q)

    #print(listasuma)



  

