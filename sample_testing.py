"""Get two strings from user,

string1: wikipedia
string2: typescript

Identify middle chars of both strings

output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
#ANSWER
string123=input()
string456=input()
print(ord(string123[int(len(string123)/2)])++ord(string456[int(len(string456)/2)]))
"""
"""
Get two integers from user

int1: 123
int2: 456

output: 123456579 (concatenation of int1,int2 and addition of two integers)
#ANSWER
int1=123
int2=456
print(str(int1)+str(int2)+str(int1+int2))
"""
"""

Collect three strings from user
String format: (name<space>float)

string1: "ravi 10.30"  
string2: "meghala 12.19"
string3: "Gokul 20.20"
split + indexing

10.30 + 12.19 + 20.20 ===> output 42.69

#ANSWER
string1="ravi 10.30"
string2="meghala 12.19"
string3="Gokul 20.20"
print(float(string1.split(' ')[1])+float(string2.split(' ')[1])+float(string3.split(' ')[1]))

#ANSWER
Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]
print(Li1[3])
print(Li1[4][1])
print(Li1[4][4][1])
print(Li1[4][4][3][2][1])
print((Li1[4][4][3][2][2])[0]+(Li1[4][4][3][2][3])[4:6])
print(Li1[4][4][3][0])
 

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "botany" from above dictionary
#Extract "gebra" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"
dic={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#ANSWER
print((dic.get(3))[0][(dic.get(3))[0].index('-')+1:])
print(tuple(dic.keys()))
print(tuple(dic.values()))
print(dic.get(2)[0]+dic.get(2)[1]+dic.get(2)[2])

Task6:
Get two strings from user:

string1: python
String2: java

output ===> jythonpava64hv (string2 first letter + string1 except first letter + string1 first letter + string2 except first letter + len of str1 + len of string2 )
"""
"""
#ANSWER
string1="python"
string2="java"
print(string2[0]+string1[1::]+string1[1]+string2[1::]+str(len(string1))+str(len(string2)))

"""""
"""
#ANSWER
str1="madam"
print(str1)
str2=list(str1)
str2.reverse()
str3="".join(str2)
if str3==str1:
    print("both string match")
else:
    print("doesnt match")
print("complete")
"""
