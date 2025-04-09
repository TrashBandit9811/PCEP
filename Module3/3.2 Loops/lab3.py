secret_word = "chupacabra"

while True:
    user_guess = input("Enter your guess: ")
    if user_guess == secret_word:
        break
    print("Haha! That is not the secret word!")

print("You guessed correctly!")