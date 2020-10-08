import math

def primefactors(number):
    factors = {}
    if number%2==0:
        factors[2] = 1
        number /= 2
    while number%2==0:
        factors[2] += 1
        number /= 2

    number_root = int(math.sqrt(number))
    for i in range(3,number_root+1,2):
        while number%i==0:
            if i in factors:
                factors[i]+= 1
            else:
                factors[i] = 1
            number /= i

    if number>1:
        factors[int(number)] = 1
    return factors

def prime(number):
    if number<2:
        print("Not a prime number. ")
    for i in range(2,number//2):
        if number%i==0:
            return "Not a prime number. "
    return "It is prime. "

number = int(input("Enter number to display prime factors: "))
factors = primefactors(number)
print(f"\nThe primefactors of {number} are:\n")
for i in factors:
    print(f"{i} - {factors[i]} times.")

print()
num = int(input(f"Enter number to check wether it is a prime number or not. "))
print(prime(num))
