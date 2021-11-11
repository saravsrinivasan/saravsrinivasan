car={"ford":"2015","bmw":"2018","nissan":"2018"}

x=car.keys()
car["honda"]="2019"
print(x)
print(car)
car.pop("honda")
car.popitem()

car["honda"]="2019"
print(car)


#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
a=set({7,8,9,1,2,3,4,5,0})
print(a)
#update set2 with 4,5,6,0
b=set({4,5,6,0})
print(b)
#check whether set2 is subset of set1 or no ?
print(a.issubset(b))
#check whether both have common elements are no ?
print(a.isdisjoint(b))
#remove 8 from set 1 and set 2 ==> find the inferences
a.remove(8)
print(a)
b.discard(8)
print(b)
print(a.intersection(b))

#discard 0 from set1 and set2
a.discard(0)
b.discard(0)
#find collection of both sets ===> set1 and set2
a.union(b)
print(a)

#create a dictionary
subj={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(subj)
a=subj.get(3)
print(a[0])
print(a)
print(type(a))

#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from abo


a = [12,13,15,[201,202,203,204],[1000,1001,1002,1003],[50,51,52,"welcome to python"]]
print(a)
print(a[2])
#15
#204
b=a[3]
print(b[3])
#1002
b=a[4]
print(b[2])
#52
b=a[5]
print(b[2])
#python
b=a[5]
c=b[3]
d=c.split(' ')
print(d[2])
a=9
b=3
if a!=b:
   print("greeater")