import random

# Need a list of answers
answers = ["Yes", "OK", "Dunno", "Nope", "Why are you asking me this?", "Doubtful", "Maybe", "It depends", "Ask later"]

# Need to be able to ask a question
while str(input("Do you have a question for the Magic 8Ball? Yes or No    ")) != 'No':
    str(input("What is your question?    "))
    # Need to return a random answer
    r = answers[random.randint(0, len(answers) - 1)]
    print(r)
else:
    print("Good Bye")


answer = random.randint(1, 50)
# The player will have a certain number of guesses
guess_count = range(1, 6) # 5 guesses
print("I am thinking of a number between 1 and 50.")

# Ask you/player what is your guess
for guess_taken in guess_count:
    guess_number = len(guess_count) - guess_taken + 1
    print("You have " + str(guess_number) + " guesses. What is your guess?")
    guess = int(input())
# If guess too high -> tells you that it is too high
    if guess > answer:
        print("Your guess is too high!")
# If guess too low -> tells you that it is too low
    elif guess < answer:
        print("Your guess is too low!")
    else:
        break # Our answer is correct

if guess == answer:
    print("Awesome!!! You guessed the number in " + str(guess_taken) + " guesses. You rock!")
else:
    print("Nope. The number I was thinking about was " + str(answer))