import os
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        print(f"Analyzing book found at {filepath}")
        file_contents = f.read()
        return file_contents

def list_of_books():
    print("Available books:")
    try:
        book_files = os.listdir("books")
        book_list = []
        counter = 1
        for book in book_files:
            if book.endswith(".txt"):  # Only show text files
                print(f"{counter}. books/{book}")
                book_list.append(f"books/{book}")
                counter += 1
        return book_list
    except FileNotFoundError:
        print("Books directory not found!")
        return []

def select_book():
    book_list = list_of_books()
    if not book_list:
        print("No books available to select.")
        sys.exit(1)
    while True:
        try:
            choice = input("\nEnter the number of the book you want to analyze (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Exiting program. Goodbye!")
                sys.exit(0)
                
            book_index = int(choice) - 1
            
            if 0 <= book_index < len(book_list):
                return book_list[book_index]
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Please enter a number or 'q' to quit.")