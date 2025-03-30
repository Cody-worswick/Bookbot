import sys
from stats import get_word_count
from stats import get_letter_count
from stats import sort_count
def get_book_text(filepath):
    with open(filepath) as f:
        print(f"Analyzing book found at {filepath}")
        file_contents = f.read()
        return file_contents
def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1] 
        text = get_book_text(book_path)
        # Get word count
        words = get_word_count(text)
        # Get letter count (character counts)
        char_count = get_letter_count(text)
        # Sort the letter counts
        sorted_counts = sort_count(char_count)
        # Print the results
        print("----------- Word Count ----------")
        print(f"Found {words} total words found in the document")
        print("----------- Character Count -------")
        for entry in sorted_counts:
            print(f"{entry['char']}: {entry['count']}")
    # Call main function
main()
