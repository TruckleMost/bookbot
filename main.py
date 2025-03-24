import sys
from stats import get_num_words
from stats import character_count
from stats import sort_by

    
def get_book_text(filepath):
    with open(filepath) as f: 
        return f.read()
    
# Check if filepath was provided as an argument
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
        
filepath = sys.argv[1]
text = get_book_text(filepath)
word_count = get_num_words(text)
print(f"Found {word_count} total words")

char_count = character_count(text)
print(char_count)

sorted_dictionary = sort_by(char_count)
# Print each character and its count, but only if it's alphabetic
for char_dict in sorted_dictionary:
    char = char_dict["char"]
    count = char_dict["count"]
    if char.isalpha():  # Only print alphabetic characters
        print(f"{char}: {count}")