num=int(input("entere any number: "))
if(num>0):
    print (f"the {num} is positvie  ")
elif(num<0):
    print(f"the {num} is negeative : ")
else :
    print(f"the {num} is zero : ") 



#cheack leap year or not
    
year=int(input("enter any year : "))
if((year % 4== 0 and year % 100 !=0) or (year % 400 == 0)):
    print(f"this is {year} is a leap year:  ")
else:
    print(f"this is {year} is not leap year ")        



#cheak even or odd number
    
num=int(input("enter any number:  " ))
if(num%2==0):
    print(f"the {num} is even number: ")

else:
    print(f"the {num} is odd number: ")