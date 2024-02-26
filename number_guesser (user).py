import random

def get_positive_integer(prompt):
    """
    Repeatedly prompts for an integer until a valid positive integer is received.

    Args:
        prompt (str): The message to display when prompting for input.

    Returns:
        int: The valid positive integer input.
    """

    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def guess_the_number():
    
    number1 = get_positive_integer("Enter the first number: ")
    number2 = get_positive_integer("Enter the second number: ")

    # Ensure user input creates a valid range with a difference
    if number1 == number2:
        print("Please enter distinct numbers for the lower and higher bounds.")

    sort = [number1, number2]
    lowest_num = min(sort)
    highest_num = max(sort)

    # Randomly choose the target number within the corrected range
    random_number = random.randint(lowest_num, highest_num)

    # Keep track of the number of guesses. Put on 1 to track the first guess
    guesses = 1

    while True:
        # Simulate the user's guess with a random number within the range
        user_guess = get_positive_integer(f"Guess a number between {lowest_num} and {highest_num}: ")

        # Check if the simulated guess is correct
        if user_guess == random_number:
            print(f"You guessed the number! It took you {guesses} guesses.")
            break

        # Give feedback based on the simulated guess, capping it to the valid range
        if user_guess > random_number:
            # Ensure feedback reflects the upper bound
            user_guess = min(user_guess, highest_num)
            print(f"Your guess is too high. The highest number is {highest_num}.")
        else:
            # Ensure feedback reflects the lower bound and doesn't go below it
            user_guess = max(user_guess, lowest_num)
            print(f"Your guess is too low. The lowest number is {lowest_num}.")

        guesses += 1

# Play the game
guess_the_number()