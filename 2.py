def linearsearch(arr,number):
    length = len(arr)
    for i in range(length):
        if arr[i]==number:
            return i
    return -1

def binarysearch(arr,number):
    length = len(arr)
    left_limit = 0
    right_limit = length - 1
    middle_index = 0

    while left_limit<=right_limit:
        middle_index = (left_limit+right_limit)//2
        if arr[middle_index]<number:
            left_limit = middle_index + 1
        elif arr[middle_index]>number:
            right_limit = middle_index - 1
        else:
            return middle_index
    return False

numbers = input("Enter numbers seperated by space to accept it as list: ")
arr = list(map(int,numbers.split()))
item = int(input("Enter number to search: "))
choice = int(input("Enter '1' for linear search and '2' for binary search: "))

if choice==1:
    index = linearsearch(arr,item)
elif choice==2:
    index = binarysearch(arr,item)
else:
    print('Wrong choice! ')

if index!=-1:
    print(f"Element found at index {index}. ")
else:
    print("Element not found. ")
