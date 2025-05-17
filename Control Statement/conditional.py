# ============== if =============

x=10
if x>=15:
    print("Welcome to if-body")
print("Welcome to main body")

x=input("Enter ")
if x:
    print("Hello")
print("Welcome")

#======== if-else =============

#write a program to check given number is even or odd

num=int (input("Enter a number:"))

if num%2==0:
    print( f'given number{num} is even')
else:
    print(f'given number {num} is odd')



# ========== if-elif ==============

#white a program to check grater number

x=int (input("Enter First number:"))
y=int (input("Enter Second Number:"))
z=int (input("Enter Third Number:"))

if(x>y and x>z):
    print(x)
elif(y>x and y>z):
    print(y)
else:
    print(z)


#======= if-elif-else ===========
#DRY:- do not repeat yourself

x=int (input("Enter the number:"))