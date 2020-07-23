n = int(input())
word = input()
strings = []
for i in range(n):
    strings.append(input())

print(strings)

for i in range(len(strings) - 1, -1, -1):
    if word in strings[i]:
        strings.remove(strings[i])

print(strings)
