#!/usr/bin/env python

"""
Given two strings “s” and “t” , write a function to determine if “t” is a
permutation of “s”. A permutation is a rearrangement of letters.
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
"""

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

def is_permutation(s1, s2):
    # build a count of all the letters in a word
    letter_counts = build_dictionary(s1)
    # then compare that count to the other word letter by letter
    for letter in s2:
        if letter not in letter_counts:
            #can't be permutation!!!
            return False
        # letter is in letter counts, so start decrementing
        letter_counts[letter] -= 1
    
    # comparison - check that all values are 0
    for letter, count in letter_counts.items():
        if count != 0:
            return False
    return True

if __name__ == "__main__":
    test_vector = [
        ("anagram", "nagaram"), 
        ("rat", "car"),
        ("ratt", "rat"), # potentially an edge condition
        ("racecar", "carrace")
    ]

    for word1, word2 in test_vector:
        if is_permutation(word1, word2):
            print(f"{word1} is a permutation of {word2}")
        else:
            print(f"{word1} is NOT a permutation of {word2}")