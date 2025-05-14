#======= Dictionary ==========


d={2:'Suraj',2:21,3:'b.tech'}

print(len(d))
print(max(d))
print(min(d))
print(sum(d))
print(type(d))
print(id(d))
print(d)

#======= Dictionary Method ==========

d={'name':'Suraj','age':21,'quali':'B.tech'}

print(d.keys())
print(d.values())
print(d.items())
print(d.get('name'))
print(d.get('age'))
d.pop('age')
print(d)
d.popitem()
print(d)

l=[1,2,3,4,5,6,7,'z','p','r']
d=dict.fromkeys(l)
print(d)
d.setdefault('name','Rahul')
print(d)
d.copy()
print(d)
d.clear()
print(d)
d1={'name':'sun','age':20,'city':'bhopal'}
d.update(d1)
print(d)