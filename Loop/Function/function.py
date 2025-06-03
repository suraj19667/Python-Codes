#writes ones calls multiple
#to achive code reusability
#to avoid sequentially or non sequentially block of code repeations

'''
type:
1.user define function
2.pre-define function
'''

def first():
    pass
first()
print(first())

#======== Even Number Function ==============
def even_number(n):
    for i in range(1,n+1):
        if i<n:
            print(2*i,end=',')
        else:
            print(2*i)

print("Hello")
print("hi")
even_number(int(input("Enter any Number:")))
print("Welcome")
even_number(int(input("Enter Number:")))

#========= Odd Number Function ==========

def odd_number(n):
    for i in range(n+1):
        if i<n:
            print((2*i-1),end=',')
        else:
            print(2*i-1)
print("Odd Number")
odd_number(int(input("Enter any number:")))

#=========== Factorial Function ======
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f'factorial of {n} is {fact}')
n=int(input("Enter any value:"))
fact(n)

#====== Higher Order Functions ======

'''
1.map()
2.filter()
3.reduce()
4.lambda()
5.Decorator()
6.Generator()

'''
l=[1,2,3,4,5]
def sqr(n):
    return n**2
x=map(sqr,l)
print(x)
print(list(x))

#-----------------
l1=[2,4,6,8]
l2=[1,2,3]
l3=[5,6,7,8]
def add(x,y,z):
    return (x+y+z)
p=map(add,l1,l2,l3)
print(list(p))
#-------------------

l1=[2,3,4,5,6]
l2=[4,5,6,7,6]
l3=[2,3,4,5,6]

x=map(lambda x,y,z:x+y+z,l1,l2,l3)

print(list(x))

#===Squre of lambda

l1=[2,3,4,5,6]
x=map(lambda x:x**2,l1)
print(list(x))

#-------------------

n=int(input("Enter any number:"))
p=lambda x:["even" if x%2==0 else "odd"] #link conferehensan (white multiple life in single line)
print(p(n))

#--------------- Even Number ----------
l1=[1,2,3,4,5,6,7,8,9,10]
p=filter(lambda x: x%2==0,l1)
print(list(p))

#-------------
l1=[1,2,3,4,5,6,7,8,9,10]
p=map(lambda x:['even' if x%2==0 else 'odd'],l1)
print(list(p))

#---------find the maximum digit ---------

from functools import reduce
l=[1,2,3,4,5,7,9,8,4]
x=reduce(lambda p,q:p if p>q else q,l)
print(x)

#--------  find the minimum digit ---------

from functools import reduce
l=[1,2,3,4,5,7,9,8,4]
x=reduce(lambda p,q:p if p<q else q,l)
print(x)

#====== Decorator =========

'''
it is a higher order function as a argument and return a function 
'''
def decore(x):
    def inner(r,s):
        r=r+5
        s=s+5
        p=x(r,s)
        return p
    return inner

@decore #@=> Is Called Decore
def add(x,y):
    return x+y
z=add(5,10)
print(z)