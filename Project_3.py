import random  # Importing the random module to generate random numbers
import time  # Importing the time module to measure the duration of the quiz

# Define constants
OPERATORS = ["+", "-", "/", "*"]  # List of mathematical operators
MIN_OPERAND = 3  # Minimum value for operands
MAX_OPERAND = 12  # Maximum value for operands
TOTAL_PROBLEMS = 10  # Total number of problems to generate

# Function to generate a random math problem
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random integer for the left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # Generate a random integer for the right operand
    operator = random.choice(OPERATORS)  # Randomly pick one operator

    expr = str(left) + " " + operator + " " + str(right)  # Create a string expression of the problem
    answer = eval(expr)  # Evaluate the expression to get the answer
    return expr, answer  # Return the expression and the answer

wrong = 0  # Initialize the count of wrong answers
input("Press enter to start!")  # Prompt the user to press Enter to start the quiz
print("...........................")

start_time = time.time()  # Record the start time

# Loop through the total number of problems
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()  # Generate a problem and get the expression and answer
    while True:  # Loop until the user guesses the correct answer
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  # Prompt the user to solve the problem
        if guess == str(answer):  # Check if the user's guess matches the answer
            break  # Exit the loop if the guess is correct
        wrong += 1  # Increment the count of wrong answers if the guess is incorrect

end_time = time.time()  # Record the end time
total_time = end_time - start_time  # Calculate the total time taken
print("...................")
print("Nice Work! You finished in", total_time, "seconds!")  # Print the total time taken to complete the quiz

# Optional: print the number of wrong answers
print("You got", wrong, "problems wrong.")  # Print the total number of wrong answers
