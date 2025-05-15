#========= Set ========
#unordered collection of unique element
#represented through {} with comma , seperate objects
#indexing not support
#slicing not supported
#mutable in nature


st={2,3,4,3,2,'python','java','php'}
print(st)
print(id(st))

#======= Python methods for set ===========

st={2,3,4,3,2,'python','java','php'}

print(len(st))
print(type(st))

#======== inbuild methods ===========
#important=> add,remove and remove,discart difference
s={2,4,6,8,'python','java'}
s.add('php')
print(s)
s.update((1,2,3,4,5,5),'python')
print(s)
s.update((1,2,'suraj'), 'python')
print(s)
s.pop()
print(s)
# s.remove('java')
# print(s)
s.discard('Java')
print(s)
s1=s.copy()
print(s,s1)
print(id(s),id(s1))

#========= van diagram ========


s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2)) #union
print(s1.intersection(s2)) #intersection
print(s1.difference(s2)) #difference
print(s1.symmetric_difference(s2)) #symmetric-difference 


# update 
'''1.intersection update
    2.difference update
    3.symmetric-difference update'''

s1.intersection_update(s2)
print(s1)

s1.difference_update(s2)
print(s1)

s1.symmetric_difference_update(s2)
print(s1)

#isdisjoint

s1.isdisjoint(s2)
print(s1)

#issuperset
print(s1.issubset(s1))
print(s2.issuperset(s1))

#issubset
print(s2.issubset(s1))