#writes ones calls multiple
#to achive code reusability
#to avoid sequentially or non sequentially block of code repeations

'''
type:
1.user define function
2.pre-define function
'''

# def first():
#     pass
# first()
# print(first())

#======== Even Number Function ==============
# def even_number(n):
#     for i in range(1,n+1):
#         if i<n:
#             print(2*i,end=',')
#         else:
#             print(2*i)

# print("Hello")
# print("hi")
# even_number(int(input("Enter any Number:")))
# print("Welcome")
# even_number(int(input("Enter Number:")))

#========= Odd Number Function ==========

# def odd_number(n):
#     for i in range(n+1):
#         if i<n:
#             print((2*i-1),end=',')
#         else:
#             print(2*i-1)
# print("Odd Number")
# odd_number(int(input("Enter any number:")))

#=========== Factorial Function ======
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(f'factorial of {n} is {fact}')
# n=int(input("Enter any value:"))
# fact(n)

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