#Question 2
#swipe the number
# l=[10,20,30,40,50]
# l[0],l[-1]=l[-1],l[0]
# print(l)

#Question 3
# t=(10,20,30,40,50)
# l=list(t)
# l[0],l[-1]=l[-1],l[0]
# t=tuple(l)
# print(tuple)

#Question 4
s='python'
l=list(s)
l[0],l[-1]=l[-1],l[0]
s=''.join(l)
print(s)

#Question 1
# Very very important for interview 
n=12345
s=str(n)
l=list(s)
l[0],l[-1]=l[-1],l[0]
s=''.join(l)
n=int(s)
print(n)

#pattern

n=5
i=1
for i in range(n):
    x='A'
    for j in range(0,n):
        print(chr(ord(x)+j),end=' ')
    print()