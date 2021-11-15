# == == == == == == == == =
# Conditional
# statements
# tasks:
# == == == == == == == == =


# Get
# a
# number
# from user check

# whether
# postive or negative
# Get
# a
# number
# from user check
""""
int1=int(input())
print(type(int1))
if int1 > 0:
    print("positive")
else:
    print("negative")
print("completed")
"""

# whether
# odd or even
# Get
# a
# character
# from user check
####Answer
"""
int1=int(input())
if int1%2 == 0 :
    print("Even")
else:
    print("Odd")
print("completed")
"""
# whether
# small
# case or upper
# case
# Get
# a
# string
# from user check
####Answer
"""""
str1=input()
if str1.isupper()==True:
    print("Upper")
else:
    print("Lower")
print("completed")
"""""

# whether
# length is even or odd
# Get
# list
# from user check

# Answer


# whether
# length is odd or even

# program1
# Get one string from user
# extract middle letter of the string
# check whether middle letter is vowel or no
"""
input1="1,32,4,5"
print(input1.split(','))
"""
# program2
# Get one string from user
# Find the middle letter
# find ascii value for the middle letter
# check whether ascii value is odd or even
#Answer
""""
pg2="STRINGHYRNSOPENNGNGN"
print(pg2[len(pg2)//2])
print(ord(pg2[len(pg2)//2]))
if ord(pg2[len(pg2)//2])%2==0:
    print("even")
else:
    print("odd")
"""

# program3:
# get one string from user
# check whether length of the string is odd or even
#ANSWER
""""
pg3="STRINGHYRNSOPENNGNGNS"
print(len(pg3))
if  len(pg3)%2==0:
    print("even")
else:
    print("odd")
"""

# program4:
# Get one string from user
# check whether string is palindrome or no

"""""
pg3="SITIS"
pg31=list(reversed(pg3))
print(pg31)
if pg31==pg3:
    print("palimdrome")
else:
    print("no palimdrome")

# program5:
# Get one mark from student
# mark 0 to 100 otherwise invalid mark
# 50 + PASS otherwise FAIL
# 90 to 100 ===> A  ==> Even + Odd -
# 80 to 89 ===> B
# 70 to 79 ===> C
# 60 to 69 ===> D
# 50 to 59 ===> E
# 0 to 49 ===> FAIL
# 93 ===> A-
# 99 ===> A-
# 88 ====> B+
"""
"""
pg5=int(input())
if pg5%2!=0:
    x='-'
else:
    x=''
if pg5 >= 50:
    print("PASS")
    if pg5 >=90 and pg5<=100:
        y=x+"A"
        print("Grade",y)
    else:
        if pg5 >= 80 and pg5 <= 89:
            y=x + "B"
            print("Grade",y)
        else:
            if pg5 >= 70 and pg5 <= 79:
                y = x + "C"
                print("Grade", y)
            else:
                if pg5 >= 60 and pg5 <= 69:
                    y = x + "D"
                    print("Grade", y)
                else:
                    if pg5 >= 50 and pg5 <= 59:
                        y = x + "E"
                        print("Grade", y)
else:
    print("FAIL")
print("completed")
"""
# 78
# VALID MARK
# PASS MARK
# C+

# program6
# hackerrank Write a function

# program7
# hackerrank Python If-Else

# program8

# two strings from user
# string 1: python  ==> first + middle + last
# string 2: ptn
#Answer
"""
pg8="python"
pg88="ptn"
pg12=(len(pg8)//2)
print(pg12)
pg8m=(len(pg88)//2)
print(pg8[:1])
print(pg88[:1])
print(pg8[-1:])
print(pg88[-1:])
print(pg8[pg12])
print(pg88[pg8m])

if pg8[:1] ==pg88[:1]  and pg8[-1:]==pg88[-1:] and pg8[pg12]==pg88[pg8m]:
    print("Matches")
else:
    print("Not matches")

# valid otherwise invalid

# program9:

# two strings from user

# mathematics ===> 4 vowels
# science ==> 3 vowels

# both are equal count or not equal
"""
str1="mathematics"
str2="science"
cnt=0
i=1
x=str1
for j in (1,2):
    for i in x:
        if i in ('aeiou'):
            cnt=cnt+1
    print(cnt)
    x=str2

# program10

# get one integer from user
# armstrong or no (without using loops)

# 153 ===> 1^3 + 5^3 + 3^3
# 370 ===> 3^3 + 7^3 + 0^3
# 371 ====> 3^3 + 7^3 + 1^3

str1=str(372)
int(len(str(str1)))
if int(str1)==(int(str1[0])**int(len(str(str1))))+(int(str1[1])**int(len(str(str1))))+(int(str1[2])**int(len(str(str1)))):
    print("Amstrong")
else:
    print("not armstrong")

# program 11:
# [123, 124, 125,]  length of list odd or even

str1=[123, 124, 125,44]
if len(str1)%2==0:
    print("even")
else:
    print("odd")
# program12:
# Fizz buzz
# Get one number from user
# 5
# Multiple of 3 ==> Fizz
# Multiple of 5 ===> buzz
# Multiple of 3 and 5 ===> Fizzbuzz
# None ==> Invalid number

int1=int(input())
if int1%3==0 and int1%5==0:
    print("Fizzbuzz")
elif int1%3==0:
     print("Fizz")
elif int1 % 5 == 0:
    print("Buzz")
else:
    print("invalid")
