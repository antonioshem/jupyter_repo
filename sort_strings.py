#function that sorts words in a string
#input is a string of words, separated by spaces
#output is a string of words sorted alphabetically

def sort_words(input):
    return ''.join(sorted(words.split() key=str.casefold))
    
    
    
def sort_words(string):
    # Split the string into a list of words
    words = string.split()

    # Sort the words alphabetically, ignoring case
    sorted_words = sorted(words, key=str.lower)

    # Join the sorted words back into a string
    sorted_string = ' '.join(sorted_words)

    # Return the sorted string
    return sorted_string
