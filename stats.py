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

def get_word_frequency(text):
    words = text.lower().split()
    word_frequency = {}
    
    # Remove punctuation from words and count them
    for word in words:
        # Clean the word of common punctuation
        clean_word = word.strip('.,!?:;\"\'()[]{}')
        if clean_word:  # Skip if the word is empty after cleaning
            if clean_word in word_frequency:
                word_frequency[clean_word] += 1
            else:
                word_frequency[clean_word] = 1
    
    return word_frequency

def sort_word_frequency(word_freq):
    # Convert dictionary to list of dictionaries
    sorted_words = []
    for word, count in word_freq.items():
        sorted_words.append({"word": word, "count": count})
    
    # Sort by count (highest first)
    sorted_words.sort(reverse=True, key=lambda x: x["count"])
    
    # Return sorted list
    return sorted_words