def bubblesort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertionsort(arr):
    length = len(arr)
    for i in range(1,length):
        current_element = arr[i]

        j = i-1
        while j>=0 and current_element< arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_element
    return arr

numbers = input("Enter numbers seperated by space to accept it as list: ")
arr = list(map(int,numbers.split()))
choice = int(input("Enter '1' to do bubblesort and '2' to do insertionsort: "))
if choice==1:
    print(bubblesort(arr))
elif choice==2:
    print(insertionsort(arr))
else:
    print("Wrong choice")

