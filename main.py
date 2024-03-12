from collections import Counter

def find_most_common_words(text, num_words=5):
    """Find the most common words in the given text."""
    # Split the text into words and count occurrences
    word_counts = Counter(text.split())
    # Return the most common words
    return word_counts.most_common(num_words)

def main():
    """Main function to demonstrate the usage."""
    # Example text
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
    # Find the most common words
    common_words = find_most_common_words(text)
    # Print the results
    print("Most common words:")
    for word, count in common_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()