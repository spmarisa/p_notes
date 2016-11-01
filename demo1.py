lettercounts = {}

for letter in "phaneendra":
    lettercounts[letter] = lettercounts.get(letter, 0) + 1

lettercounts.sort()
print(lettercounts)

