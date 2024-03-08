#reverse string
def reverse(string):
    string = string[::-1]
    return string
 
s = "ENGINEER"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))


#cheek palidrome

strings = input("enter any word : ")
j = -1
flag = 0
for i in strings:
    if i != strings[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("this is not palidrome ")
else:
    print("this is palidrome  ")




#coutn charactr
character=input("enter any word : ")
count=0
for i in character:
    count=count+1
print(count)        
