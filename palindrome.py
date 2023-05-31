#write a python function that determines if a given string is a palindrome
#palindrome is a word or phrase that reads the same forwards as backwards
#for example level or racecar
###### conditions
# input is a string for evaluation
# output is a boolean value
# only consider letters between A and Z inclusive
# ignore cases 
# example is_palindrome('hello world') should return false while is_palindrome("go hang a salami - I'm a lasagna hog.") it returns true


def is_palindrome(string):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_string = ''.join(ch.lower() for ch in string if ch.isalpha())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

input_words = input("Enter the word to check if it's a palindrome: ")
is_palindrome_result = is_palindrome(input_words)
print(is_palindrome_result)


#solution 2

import re
def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards