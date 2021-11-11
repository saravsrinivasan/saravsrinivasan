#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
x=(1,4,5,6,7,8)
y=(5,6,7,8,9)
print(x)
print(y)
#Find the common elements between two tuples
x1=set((x))
y1=set((y))
z=x1.intersection(y1)
print(z)
#Concatenate both tuples and remove duplicates from tuple
z=x1.union(y)
print(z)
#Find the index value of 9 (after concatenation)
x = (1, 4, 5, 6, 7, 8)
y = (5, 6, 7, 8, 9)
z=x+y
print(z.index(9))
#multiply above elements 3 times
print(z*3)



#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2
#find collection of both sets ===> set1 and set2
