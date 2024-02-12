import random
import math

# Taking Inputs
lower = int(input("Enter Lower bound:- "))  # Asking the user to input the lower bound of the range.

# Taking Inputs
upper = int(input("Enter Upper bound:- "))  # Asking the user to input the upper bound of the range.

# generating random number between the lower and upper bounds
x = random.randint(lower, upper)  # Generating a random integer within the specified range.
print("\n\tYou've only ", 
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")  # Informing the user about the number of chances based on the range.

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):  # Looping until the number of guesses exceeds the minimum required guesses.
	count += 1  # Incrementing the count for each guess.

	# taking guessing number as input
	guess = int(input("Guess a number:- "))  # Asking the user to guess the number.

	# Condition testing
	if x == guess:  # If the guessed number is correct.
		print("Congratulations you did it in ",count,"try")  # Printing success message.
		# Once guessed, loop will break
		break
	elif x > guess:  # If the guessed number is too small.
		print("You guessed too small!")
	elif x < guess:  # If the guessed number is too large.
		print("You Guessed too high!")

# If Guessing is more than required guesses, shows this output.
if count > math.log(upper - lower + 1, 2):  # If the user exceeds the number of guesses allowed.
	print("\nThe number is %d" % x)  # Revealing the correct number.
	print("\tBetter Luck Next time!")  # Providing an encouragement message.

# Better to use This source Code on PyCharm!
