#two number sum with  fucnton differet arguments


def cal_sum(num1,num2):
    return num1+num2



first_arg=cal_sum(50,100)
print("the fist  sum is ",first_arg)

second_arg=cal_sum(50,50)
print("the second sum is  ",second_arg)

third_arg=cal_sum(10,20)
print("the thies  sum is : ",third_arg)

#cheak prime number with fucntion

def is_prime(number):
   
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [2, 3, 17, 25, 29, 31]

for num in numbers:
    if is_prime(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")



