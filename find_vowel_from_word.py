#Pseudocode: for finding vowels in strings we have to provide a function that matches with vowels, 
# if matches it gives output or else code goes wrong.

vowels_array = ['a', 'e', 'r', 'o', 'p', 'l', 'a', 'n', 'e']

def check_vowels_in_words(string):
    if vowels_array in string:
        print("entered words contains vowel in it")
    else:
        print("entered words contains no vowels in it")