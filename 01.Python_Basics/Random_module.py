import random
import string


# This is a simple OTP generator.
"""
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp
    
print("Your OTP is:", generate_otp())
"""


# This is a simple number guessing game.
"""
target_number = random.randint(1, 100)
while True:
    guess = input("Guess a number between 1 and 100 or Quit(Q): ")
    if guess == 'Q' or guess == 'q':
        print("You have quit the game.")
        print("The target number was:", target_number)
        break
    guess = int(guess)
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
"""

# This is a simple password generator.
n = int(input("Enter the length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation

result = "".join([random.choice(characters) for i in range(n)])
#  or print("".join(result))
print("Your password is:", result)

password = ""
for i  in range(n):
    password += random.choice(characters)
print("Your password is:", password)
