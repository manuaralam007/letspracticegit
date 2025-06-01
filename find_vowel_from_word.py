#Pseudocode: for finding vowels in strings we have to provide a function that matches with vowels, 
# if matches it gives output or else code goes wrong.

vowels_array = 'aeiou'

def check_vowels_in_words(vowels_str):
    if any(vowel in vowels_str for vowel in vowels_array):
        print("entered words contains vowel in it")
    else:
        print("entered words contains no vowels in it")

check_vowels_in_words("aeroplane")
