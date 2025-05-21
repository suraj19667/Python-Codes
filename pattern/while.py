# pattern matching 
# 1

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(''*i)     or ''i+' '(n-i)
#     i+=1



# 2
 
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(' '(n-i)+''*i)
#     i+=1

# 3
 
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(' '(n-i)+' '*i)
#     i+=1


# 4
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(''(n-i)+' '*i)
#     i+=1

# 5
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(' 'i+''*(n-i))
#     i+=1

# 6
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(' 'i+' '*(n-i))
#     i+=1


#7
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(' 'i+' '*(n-i))
#     i+=1
# i=i-2
# while i>=0:
#     print(' 'i+' '*(n-i))
#     i-=1

#8
# n=int(input("Enter a number: "))
# i=0
# while i<n:
#     print('* '*(n-i))
#     i+=1
# i=i-2
# while i>=0:
#      print('* '*(n-i))
#      i-=1    

# 9
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(' '(n-i)+' '*i)
#     i+=1
# i=i-2
# while i>0:
#     print(' '(n-i)+' '*i)
#     i-=1

#===== Armstrong Number ========
#Write a program to find total number of digits in given number

# n=int(input("Enter a Number:"))
# x=str(n)
# print(len(x))
# digit=0
# while n>0:
#     n=n/10
#     digit=digit+1
# print(f'total digit is{digit} in given number {n}')
#write a program to find total sum of digits in given number
# n=int(input("Enter a number:"))
# sum=0
# while n>0:
#     last_digit=n%10
#     sum=sum+last_digit
#     n=n//10
# print(f'total sum is :{sum}')

#Armstrong Number
# n=int(input("Enter a number:"))
# digit=1
# sum=0
# x=y=n
# while n>0:
#     digit=digit+1
#     n=n//10
# while n>0:
#     last_digit=x%10
#     sum=sum+last_digit**digit
#     x=x//10

#     if y==sum:
#         print(f'given no {y} is armstorng')
#     else:
#         print(f'not a armstrong number')


#palindrom

# n=input("enter any number:")
# if n==n[::-1]:
#     print(f'give value {n} is palindrom')
# else:
#     print(f'given value {n}is not palindrom')

# n=int(input("enter any thing"))
# rev=0
# while n>0:
#     last_digit=n%10
#     rev=rev*10+last_digit
#     n=n//10
# if n==rev:
#     print(f'given number is{x} palindrom')
# else:
#     print(f'not palindrom{x}')


#string reverse with convensional method

s=str(input("Enter any String:"))
rev=s[::-1]
print(rev)