consonents = 'bcdfghjklmnpqrstvwxyz'
string = input("Enter string: ").split()
longest_word = ""
for word in string:
    boolean = True
    for letter in word:
        if letter not in consonents:
            boolean = False
            break
    if boolean and len(word)>len(longest_word):
        longest_word = word
print(longest_word)

