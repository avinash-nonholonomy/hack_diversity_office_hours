#!/usr/bin/env python
"""
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of
letters.
Input: Tact Coa
Output: true (permutation “taco cat”, “atco cta”, etc.)
"""

from q1_word_frequency import build_dictionary
import math

# first, what makes a palindrome?
# Iterate forward and backward and if they're the same, it's good
# it's not just the letters, it's the order
# strings have lengths, so we can use one index and some math!
"""
 racecar
 0     6
  1   5
   2 4 #stop here with floor
    33 #ceil would go here
"""
# Not asked for (or required in the final answer), but it can help to 
# understand the rest of the problem.
def is_palindrome(string):
    string = string.replace(" ", "")
    for i in range(0, math.floor(len(string)/2)): # Had a question on how to handle the middle character. It can be anything and still be a palindrome, but it's nice to know how to stop before or after by using ceil or floor round functions.
        if string[i] != string[len(string)-1-i]:
            return False
    return True

# In the section we had a lot of trouble (myself included!) coming up with the 
# key insight of what makes something permutable into a palindrome. To get some 
# insight we analyzed the letter counts (using the function from q1) of a set of
# palindromes to see what was unique about those:
def generate_insight(words):
    print("#"*60)
    print("Trying to get some insight...")
    for word in words:
        word = word.replace(" ","") # remove spaces
        if is_palindrome(word):
            print(word, build_dictionary(word))
    print("#"*60)
# generate_insight outputs this: 
"""
############################################################
Trying to get some insight...
bbabcddcbabb {'b': 6, 'a': 2, 'c': 2, 'd': 2}
babcddcbab {'b': 4, 'a': 2, 'c': 2, 'd': 2}
abcddcba {'a': 2, 'b': 2, 'c': 2, 'd': 2}
bcddcb {'b': 2, 'c': 2, 'd': 2}
racecar {'r': 2, 'a': 2, 'c': 2, 'e': 1}
racxcar {'r': 2, 'a': 2, 'c': 2, 'x': 1}
tacocat {'t': 2, 'a': 2, 'c': 2, 'o': 1}
atcocta {'a': 2, 't': 2, 'c': 2, 'o': 1}
############################################################
"""
# If we look at this we can see that palindromes of even length can only have 
# even counts! That's the key insight. If the string is odd you can have at 
# most one non-even count.

# permadrome is a portmantaue of permutation and palindrome... say that ten times fast!
def is_permadrome(string):
    letter_counts = build_dictionary(string)
    number_of_odd_counts = 0
    for count in letter_counts.values():
        if count % 2 != 0: # see if it's odd
            number_of_odd_counts += 1
            if number_of_odd_counts >= 2:
                return False
    return True

if __name__ == "__main__":
    # always add more tests than what they ask for, shows that you think ahead to find edge conditions!
    test_vector = [
        "bbabcddcbabb",
        "babcddcbab",
        "abcddcba",
        "bcddcb",
        "racecar",
        "racxcar",
        "anagram",
        "nagaram", 
        "carrace",
        "taco cat",
        "atco cta",
    ]
    generate_insight(test_vector)

    # Run a test on a bunch of different words!
    print("Running test on permadrome")
    for word in test_vector:
        word = word.replace(" ", "")
        print(word, is_permadrome(word))
    