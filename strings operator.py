# str1="Prasad"
# str2="Achari"
# str3=str1+ " "+str2
# print(str3)
# str3=str1-str2
# print(str3)
# str3=str1/str2
# print(str3)
# str3=str1*str2
# print(str3)
# str3=str1*4
# print(str3)

'''reversing a strings and sentence
str=input("enter the string")
rev=""
for i in str:
    rev=i+rev
print(rev) '''  

'''str=input("enter the string")
print(str)
str1=str.split()
rev=""
for i in str1:
    rev=i+" "+rev
print(rev) 
'''
# removing the sapces from end and front
# str=input("enter the string")
# print(str)
# str1=str.lstrip()
# print(str1)
# str2=str.rstrip()
# print(str2)
# str3=str.strip()
# print(str3)

# 2 eg
'''str=input("enter the string")
str1=" "
for i in str:
    if i==" ":
        pass
    else:
        str1=str1+i
print(str1)'''
# check wether string contains num,digi,both
str=input("enter the string")
if str.isalpha():
    print("contains only alpha")
elif str.isdigit():
    print("contains only digit")
elif str.isalnum():
    print("contains only both")
else:
    print("contains special cchar")


