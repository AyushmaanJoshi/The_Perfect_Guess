import random

def play_game():
    random_number = random.randint(1, 10)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?\n")

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("⚠️ Please enter a number between 1 and 10.")
                continue

            if guess > random_number:
                print("🔻 Too high! Try a smaller number.\n")
            elif guess < random_number:
                print("🔺 Too low! Try a bigger number.\n")
            else:
                print(f"✅ Congratulations! You guessed it right 🎉\nThe number was: {random_number}")
                print(f"📈 Total attempts: {attempts}\n")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a **valid integer** between 1 and 10.\n")

while True:
    play_game()
    again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("👋 Thanks for playing! See you next time.")
        break
