string = input()
index = len(string)
reversedString = ""
while index > 0:
    index -= 1
    reversedString += string[index]

print(reversedString)

word = input()
reversedWord = ""
for i in range(len(word) - 1, -1, -1):
    reversedWord += word[i]

print(reversedWord)
