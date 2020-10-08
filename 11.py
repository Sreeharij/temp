file = input("Enter name of file(including '.txt' extension): ")
with open(file,'rt') as f:
    data = f.readlines()
words = []
for line in data:
    for word in line.split():
        words.append(word)
freq_map = {}
for i in words:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1

for word in freq_map:
    print(f"'{word}' - {freq_map[word]} times")
