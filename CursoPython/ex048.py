s = 0
count = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        s = s + c
        count = count + 1
print(s)
print(count)