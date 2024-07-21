with open("story.txt", "r") as f:  # Open the file "story.txt" in read mode.
    # The 'with' syntax is used to create a context for file operations, ensuring the file is properly closed after the operations are done.
    story = f.read()  # Read the entire content of the file and store it in the variable 'story'.

words = []  # Initialize an empty list to store words found within target delimiters.
start_of_word = -1  # Initialize the start position of a word.

target_start = "<"  # Define the target start delimiter.
target_end = ">"  # Define the target end delimiter.

# Loop through each character in the story, along with its index.
for i, char in enumerate(story):
    if char == target_start:  # Check if the character matches the start delimiter.
        start_of_word = i  # Set the start position of the word.

    if char == target_end and start_of_word != -1:  # Check if the character matches the end delimiter and a start was found.
        word = story[start_of_word:i + 1]  # Extract the word including the delimiters.
        words.append(word)  # Add the word to the list.
        start_of_word = -1  # Reset the start position.

answers = {}  # Initialize an empty dictionary to store user inputs for each word.

# Loop through each word found within the delimiters.
for word in words:
    answer = input("Enter a word for " + word + ": ")  # Prompt the user for a replacement word.
    answers[word] = answer  # Store the user input in the dictionary with the word as the key.

print(answers)  # Print the dictionary containing user inputs.
