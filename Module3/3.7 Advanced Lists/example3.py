
squares = [x ** 2 for x in range(10)]

odds = [x for x in squares if x % 2 != 0 ]

print(odds)

# Output: [1, 9, 25, 49, 81]
