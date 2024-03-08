li_st=[1,2]
print("the current list: ")
print(li_st)

li_st.append(3)
li_st.append(4)
li_st.append(5)
li_st.append(6)
print("the list  adding new value ")
print(li_st)
print("acces the element wiht index number: ")
print("the fisr element of  lists is : ",li_st[0])
print("the secodn element of  lists is : ",li_st[1])
print("the fourth  element of  lists is : ",li_st[3])

print("the reombvig element of lists : ")
li_st.pop(0)
li_st.pop(1)

print("the current elemt of lists after removig :  ")
print(li_st)


#ttupele implemt (name,age ,gender)

person = ("Robiul ",22,"male ")


name = person[0]
age = person[1]
gender = person[2]


print("Name:", name)
print("Age:", age)
print("Gender:", gender)


#the dictonary programe

student = {
    "name": "robil",
    "age": 23,
    "grade": 4.00
}

# Print the values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])


