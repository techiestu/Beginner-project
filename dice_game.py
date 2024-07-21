# class abc:
#     pass #this is an empty class
# class Employee:
#     def putdata(self):
#         self.id = int(input("Enter employee ID: "))
#         self.name = input("Enter employee name: ")
#         self.salary = float(input("Enter employee salary: "))
#
#     def display(self):
#         print("Employee ID:", self.id)
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
#
#
# # Instantiate the Employee class
# a = Employee()
#
# # Call the methods
# a.putdata()
# a.display()


# import random          ##allow user to generate random number
# def roll():            ##define a function roll(that is reusable block of code) (def is defined you)
#     min_value =1
#     max_value = 2
#     roll = random.randint(min_value, max_value)
#     return roll
#
# # value= roll()
# # print(value)
#
# #Asking user how many players are going to participate.
# while True:
#     players = input("enter the no of players (1-4): ")
#     if players.isdigit():       #isdigit going to tell us that it is digit or not
#         players =int(players)
#         if 1<= players <=4:
#             break
#         else:
#             print("Must be between 2-4 players.")
#     else:
#         print("Invalid, try again.")
# # print(players)
#
# max_score =50
# players_scores = [o for _ in range(len(players))]
# # print(players_scores)
#
# while max(players_scores) < max_score:
#     should_roll = input("would you like to roll (y)? ")
#     if should_roll.lower() !="y":
#         break
#     value = roll()
#     if value ==1:
#         print("You rolled a 1! Turn done!")
#         break
#     else:
#         current_score +=value
#         print("you rolled a:", value)
#     print( "your score is: ", current_scorre)



import random  # Importing the random module to generate random numbers

def roll():  #define a function roll(that is reusable block of code) (def is defined you)
    min_value = 1  # Minimum value for the dice roll
    max_value = 2  # Maximum value for the dice roll
    roll = random.randint(min_value, max_value)  # Generate a random number between min_value and max_value
    return roll  # Return the generated number

# Asking user how many players are going to participate
while True:
    players = input("Enter the number of players (1-4): ")  # Prompt user for number of players
    if players.isdigit():  # Check if the input is a digit
        players = int(players)  # Convert input to an integer
        if 1 <= players <= 4:  # Check if the number of players is between 1 and 4
            break  # Exit the loop if the number of players is valid
        else:
            print("Must be between 1-4 players.")  # Inform the user about the valid range
    else:
        print("Invalid, try again.")  # Inform the user about invalid input

max_score = 50  # Maximum score to win the game
players_scores = [0 for _ in range(players)]  # Initialize scores for each player

# Main game loop
while max(players_scores) < max_score:  # Continue the game until a player reaches the maximum score
    for i in range(players):  # Loop through each player
        current_score = players_scores[i]  # Get the current score of the player
        while True:  # Loop for rolling the dice
            should_roll = input(f"Player {i+1}, would you like to roll (y)? ")  # Ask the player if they want to roll
            if should_roll.lower() != "y":  # If the player does not want to roll, break the loop
                break
            value = roll()  # Roll the dice
            if value == 1:  # If the player rolls a 1
                print("You rolled a 1! Turn done!")  # Inform the player
                break  # End the player's turn
            else:
                current_score += value  # Add the rolled value to the current score
                print("You rolled a:", value)  # Show the rolled value
            print("Your score is:", current_score)  # Show the current score

        players_scores[i] = current_score  # Update the player's score
        if current_score >= max_score:  # Check if the player has reached the maximum score
            print(f"Player {i+1} wins with a score of {current_score}!")  # Announce the winner
            break  # End the game
    if current_score >= max_score:  # If a player has won, break the outer loop
        break

# Optional: Print final scores
for i, score in enumerate(players_scores):
    print(f"Player {i+1} final score: {score}")
