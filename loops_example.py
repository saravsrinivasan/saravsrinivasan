"""
list_user = int(input("enter number of list:"))
l = {}
for x in range(0,list_user):
    l.update({input(): input()})
print("final list",l)
"""


####TASK 3
"""
Li1 = [3,4,5,2,7,8,9,10]
odd = []
even = []
for i in Li1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("odd:",odd)
print("even:",even)

#### TASK 4
#get one list form user
#separatre positive and negative
inp = [4,-5,3,4,5,-6,-9]
pos=[]
neg=[]
for i in inp:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
print("pos:",pos)
print("neg:",neg)


Taks5:
Get list of strings from user
separate it in to two lists with vowles and non vowels 
No of elements with vowel: 4
No of elements without vowel: 3

inp=["hi","ggg","hello","ravi","bbbb","zzz","yyyy"]
v=0
n=0
for i in inp:
    if ('a' in i) or ('e' in i) or ('i' in i) or ('o' in i) or ('u' in i):
        v=v+1

print("vowel:",v)
print("without vowelL",len(inp)-v)
print("complete")


Task6:

Get list of strings from user
separate it two list (with same first letter and last letter and othr)

["garg", "kohli", "rohitr", "ishan", "dhoni","dad"]

No of elements with same first letter and last letter: 3
Other List: 3

inp=["garg", "kohli", "rohit", "ishan", "dhoni","dad"]
cnt=0
cnt_el=0
for i in inp:
    if i[:1] == i[-1:]:
        cnt = cnt+1
    else:
        cnt_el = cnt_el+1
print("No of elements same:",cnt)
print("Other:",cnt_el)


n = int(input())
l=[]
x=0
i=0
y=1
while i <= n:
      if x==0  :
         l.append(x)
         x=1
      else:
          x = i+y
          l.append(x)
          y = i
          i = x

print("Fibonacci Series:",l)



arm=input()
y=0
for i in range(len(arm)):
    y = (int((arm)[i])**int(len(arm)))+y
print(y)
if int(arm)==y:
    print("Armstrong")
else:
    print("Not armstrong")

prime=input()
x=0
flag=True
for i in range(2,int(prime)-1):
    if int(prime)%i==0:
        flag = False
        break
if flag:
    print("prime")
else:
    print("Not prime")



ana=input()
str1=""
x=0
for i in range(1,len(ana)+1):
      x=len(ana)-i
      str1=str1+ana[x]
print("str1:",str1)
if str1==ana:
    print("Anagram")
else:
    print("No")


#sum of digits

sum=input()
x=0
for i in range(len(sum)):
      x= x+int(sum[i])
print("Sum:",x)


#multiples of a number

mult=input()
x=0
str1=""
for i in range(1,int(mult)+1):
    if int(mult)%i==0:
        if i==1:
            str1 = str(i)
        else:
            str1 = str1 + "," + str(i)
print("multiply:",str1)
"""