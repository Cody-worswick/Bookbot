import sys
from stats import get_word_count, get_letter_count, sort_count, get_word_frequency, sort_word_frequency
from file_utils import get_book_text, select_book

def main():
    print("============ BOOKBOT ============")
    
    while True:  # Main program loop
        if len(sys.argv) > 1 and len(sys.argv[1].strip()) > 0:
            book_path = sys.argv[1]
            # Clear sys.argv so next loop will show menu
            sys.argv = [sys.argv[0]]  
        else:
            print("Usage: python3 main.py <path_to_book>")
            print("Or you can choose from these books:")
            book_path = select_book()
        
        text = get_book_text(book_path)
        # Get word count
        words = get_word_count(text)
        print("----------- Word Count ----------")
        print(f"Found {words} total words found in the document")
        
        # Ask user what analysis they want to perform
        while True:
            analysis_choice = input("\nWhat would you like to analyze? (1) Character frequency (2) Word frequency: ")
            if analysis_choice == "1":
                # Get letter count (character counts)
                char_count = get_letter_count(text)
                # Sort the letter counts
                sorted_counts = sort_count(char_count)
                print("----------- Character Count -------")
                for entry in sorted_counts:
                    print(f"{entry['char']}: {entry['count']}")
                break
            elif analysis_choice == "2":
                # Get word frequency
                word_freq = get_word_frequency(text)
                # Sort the word frequency
                sorted_words = sort_word_frequency(word_freq)
                print("----------- Top 20 Words -------")
                for entry in sorted_words[:20]:  # Limit to top 20
                    print(f"{entry['word']}: {entry['count']}")
                break
            else:
                print("Please enter 1 or 2.")
            
        # Ask if user wants to analyze another book
        while True:
            choice = input("\nWould you like to analyze another book? (y/n): ")
            if choice.lower() == 'y':
                break  # Break this inner loop and continue the main loop
            elif choice.lower() == 'n':
                print("Thank you for using Bookbot! Goodbye!")
                return  # Exit the main function
            else:
                print("Please enter 'y' or 'n'.")

# Call main function
if __name__ == "__main__":
    main()