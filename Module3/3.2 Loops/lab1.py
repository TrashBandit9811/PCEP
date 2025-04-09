secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""
)

picked_number = int(input("Enter your guess: "))

while picked_number != 777:
    picked_number = int(input("Ha ha! You're stuck in my loop! "))

print("Well done, muggle! You are free now.")