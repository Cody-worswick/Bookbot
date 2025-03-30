def get_word_count(words):
    words_count = words.split()
    return len(words_count)
def get_letter_count(words):
    words = words.lower()
    char_count = {}
    for char in words:
        if char in char_count:
            # Character exists, increment count
            char_count[char] += 1
        else:
            # Character doesn't exist yet, add it
            char_count[char] = 1  
    return char_count
def sort_count(char_count):
    # Convert the dictionary into a list of dictionaries
    char_list = [{"char": char, "count": count} for char, count in char_count.items() if char.isalpha()]
    # Sort the list by the "count" key in descending order
    char_list.sort(key=lambda item: item["count"], reverse=True)
    return char_list