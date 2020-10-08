import random
length = int(input("Enter number of key value pairs to be stored: "))
dictionary = {}
for i in range(1,length+1):
    emp_no = int(input("Enter employee number: "))
    name = input("Enter name of employee: ")
    dictionary[i] = (emp_no,name)
lucky_winner = dictionary[random.randint(1,length)]
print()
print(f"Congragulations to {lucky_winner[1]}(employee code: {lucky_winner[0]}) for winning a gold coin for the\nnew year from the company using random function. ")

