dictionary = {6:18,3:523,1:2,2:109,10:25,12:23}
sorted_keys = list(dictionary.keys())
length = len(sorted_keys)
new_dictionary = {}
for i in range(length-1):
    for j in range(0,length-i-1):
        if sorted_keys[j] > sorted_keys[j+1]:
            sorted_keys[j],sorted_keys[j+1] = sorted_keys[j+1],sorted_keys[j]
for key in sorted_keys:
    new_dictionary[key] = dictionary[key]
print(new_dictionary)
