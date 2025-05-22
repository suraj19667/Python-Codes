# l=[1,2,3,4,5]
# l1=[]
# for i in l:
    
#     l1.append(i**2)
# print(l1)

#user input (a,b,c,d,e)=>(e,f,g,h,i)

# x='a'
# print(ord('a'))
# print(ord('a')+4)

# print(chr(ord('a')+4))

# s=input("enter string:")
# s1=()
# for i in s:
#     print(chr(ord(i)+4))


# s='abcde'
# s1=''
# for i in s:
#     chr(ord(i)+4)
#     s1=''.join((s1,chr(ord(i)+4)))
# print(s1)

# s='abcde'
# s1=''
# for i in s:
#     s1=''.join((i,s1))
# print(s1)
# if s==s1:
#     print("palindrom")
# else:
#     print("not a palindrom")

#odd even

# num=int(input("Enter a number:"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
#     if i<num:
#         print(i,end='+')

#     else:
#         print(i,end='=')
# print("Sum is:",sum)

#Even number sum

# n=int(input("Enter a Number:"))
# sum=0
# for i in range(2,n+1,2):
#     sum=sum+i
#     if i<=n-2:
#         print(i,end='+')
#     else:
#         print(i,end='=')
# print(sum)

#even number sum


n=int(input("Enter a Number:"))
sum=0
for i in range(1,n+1):
    sum=sum+(2*i)
    if i<n:
        print(2*i,end='+')
    else:
        print(2*i,end='=')
print(sum)

