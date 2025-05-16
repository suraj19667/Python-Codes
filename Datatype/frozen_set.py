#unorder unique element
#represented through frozenset() with comma, seperate elements
#indexing not supported
#slicing not supported
#inmutable in nature

l=[10,20,30,20,40]
l1=[23,40,54,20,30]
fs=frozenset(l)
print(fs)
print(type(fs))
fs1=frozenset(l)
fs2=frozenset(l1)
print(fs1.union(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.issubset(fs2))
print(fs1.issuperset(fs2))