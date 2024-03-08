
              

n=int(input("enter any number for  fibonacci series : "))

print("the fibonaci series : ")

n1=0
n2=1
count=0
if n<0 :
    print("error! plese enter positive entegr ")
elif  n== 1:
    print(n1)
else:
    while(count<n):
        print(n1)
        nextt=n1+n2
        n1=n2  
        n2=nextt
        count+=1      



#chek prime or not
num=int(input("enter any positice number: "))

flag=False
if num==1:
    print("the number is prime ")
else:
     for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
            
            
if flag==True:
        print(num, "is not a prime number")
else:
        print(num, "is a prime number")    




#check factorial number

def factorial(x):
  
    if x == 1:
        return 1
    else:
      
        return (x * factorial(x-1))



num = int(input("enter any positive number : "))

result = factorial(num)
print("The factorial of", num, "is", result)