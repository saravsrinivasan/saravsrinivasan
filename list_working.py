fruits = ['apple', 'banana', 'cherry']
fruits.append("Kiwi")
print(fruits)
veg=fruits.copy()
print(veg)
x=fruits.count("apple")
print(x)
vege=('onion','carrot','drumstick')
fruits.extend(vege)
print(fruits)
x=fruits.index("onion")
print(x)
fruits.insert(4,"watermelon")
print(fruits)
fruits.remove("drumstick")
print(fruits)
fruits.reverse()
print(fruits)
fruits.sort()
tup=(2,4,5,2,10)
y=tup.count(2)
print(y)
z=tup.index(4)
print(z)
frit={'RED','ORANGE','GREEN'}
print(frit)
frit.add("YELLOW")
print(frit)
tea=frit.copy()
print(tea)
NEW={'DUEUE','ORANGE','GREEN'}
ban=frit.difference(NEW)
print(ban)
XEP=frit.intersection(NEW)
print(XEP)
abc=frit.isdisjoint(XEP)
print(abc)
ab=frit.issuperset(NEW)
print(ab)
print(frit)
print(NEW)
ABD=frit.symmetric_difference(NEW)
print(ABD)