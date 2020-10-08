def fandsmax(arr):
    idx1 = idx2 = 0

    for i in range(1,len(arr)):
        if arr[i]>arr[idx1]:
            if arr[idx1]>arr[idx2]:
                idx2 = idx1
            idx1 = i
        elif arr[i]>arr[idx2]:
            idx2 = i
        print(idx1,idx2)
    return idx1,idx2

numbers = input("Enter list of numbers seperated by space. ")
numbers = list(map(int,numbers.split()))

index1,index2 = fandsmax(numbers)
print(f'Largest number: {numbers[index1]} at index {index1}\nSecond larges number: {numbers[index2]} at index {index2}')
