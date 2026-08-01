s1={'devanoor':'midthur','nandyal':'kurnool',5:9,7:3,'allagada':'nandyal'}
print(s1)
print(type(s1))

s1.pop(5)
print(s1)

s1.pop('devanoor')
print(s1)

s1.popitem()
print(s1)

print(s1.get('nandyal'))

print(s1.keys())
print(s1.values())

for i in  s1 . keys():
	print(s1)

for i in s1 . items():
	print(s1)

s1.setdefault('kouluru','konidedu')
print(s1)

s1['AP']='vizac'
print(s1)