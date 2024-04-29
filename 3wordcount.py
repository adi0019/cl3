

import re
from collections import defaultdict

# Function to process the text file and return character and word counts
def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()  # Read the file content
    
    # Count characters
    char_count = defaultdict(int)
    for char in text:
        char_count[char] += 1
    
    # Count words
    word_count = defaultdict(int)
    words = re.findall(r'\w+', text.lower())  # Extract words
    for word in words:
        word_count[word] += 1
    
    return dict(char_count), dict(word_count)  # Return character and word counts


# Main block to process the text file
if __name__ == "__main__":
    # Static path to the text file
    file_path = "C:/Users/Aditya/OneDrive/Pictures/input.text"  # Modify with your static file path
    
    # Get character and word counts
    char_counts, word_counts = process_text(file_path)
    
    # Display the results
    print("Character Counts:", char_counts)
    print("Word Counts:", word_counts)
