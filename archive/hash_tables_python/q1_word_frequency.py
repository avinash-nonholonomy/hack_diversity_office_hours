#!/usr/bin/env python

"""
Design a method to find the frequency of occurrences of any given
word in a book. Given the book as an array of strings and the
word as a string. What if we were running this algorithm
multiple times?
Input: book = ["always", "code", "as", "if", "the", "guy", "who", "ends", "up", "maintaining",
"your", "code", "will", "be", "a", "violent", "psychopath", "who", "knows", "where", "you", "live"]
Word = "who"
Output: 2
"""
# Note - look up collections.Counter for the built-in python way of doing this: https://docs.python.org/3/library/collections.html
def build_dictionary(words):
    # create an empty dict (hash table/associative array)
    dictionary = dict() 

    # iterate through all the input words
    for word in words:
        # if the word is already in the dictionary, increment the value
        # (less pythonic) if dictionary.has_key(word):
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def get_word_frequency(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    return 0

if __name__ == "__main__": # this is just python for run what follows
    input_word_list = ["always", "code", "as", "if", "the", "guy", "who", "ends", "up", 
    "maintaining", "your", "code", "will", "be", "a", "violent", "psychopath",
    "who", "knows", "where", "you", "live", "will", "will", "will"]

    dictionary = build_dictionary(input_word_list)
    print("dictionary", dictionary)
    # We were asked to test one value ...
    result = get_word_frequency(dictionary, "who")
    
    # but you should always test more! 
    unique_words = set(input_word_list) # get a unique list of words in the input
    for word in unique_words:
        result = get_word_frequency(dictionary, word)
        print(f"Found {result} counts of word '{word}'")
    
    # Need to also test words that werent' in the input!!!
    word = "a;sdlfkja;lsdkjfklsjdlfajsdlkfj"
    result = get_word_frequency(dictionary, word)
    print(f"Found {result} counts of word '{word}'")
