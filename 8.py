def small_digit(n):
    smallest = int(n[0])
    for i in n:
        if int(i)<smallest:
            smallest = int(i)
    return smallest

number = input("Enter number: ")
print(small_digit(number))
