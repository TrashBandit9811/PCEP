for i in range(1,11):
    if i % 2 != 0:
        print(i)

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch,end="")
print("")

for digit in "0165031806510":
    if digit == "0":
        print("X",end="")
        continue
    print(digit,end="")
print("")