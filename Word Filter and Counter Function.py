import re

def word_filter_counter(text, filter_words):
    # Convert text to lowercase for case-insensitive comparison
    text_lower = text.lower()
    
    # Initialize a dictionary to store filtered word counts
    filtered_word_counts = {}
    
    # Split the text into words using regular expression
    words = re.findall(r'\b\w+\b', text_lower)
    
    # Iterate through each word in the text
    for word in words:
        # Check if the word is in the filter_words list
        if word in filter_words:
            # Increment the count of the filtered word
            filtered_word_counts[word] = filtered_word_counts.get(word, 0) + 1
    
    return filtered_word_counts

# Example Test Cases
print(word_filter_counter("Hello world, hello!", ["hello"]))  # Output: {'hello': 2}
print(word_filter_counter("The quick brown fox.", ["the"]))  # Output: {'the': 1}
print(word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]))  # Output: {'is': 2, 'this': 2, 'just': 1}
print(word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]))  # Output: {'we': 1, 'the': 1, 'or': 1}
