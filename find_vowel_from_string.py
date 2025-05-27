# this function will tell you about finding strings into vowels
# we have to give a string_list(a,e,i,o,u, A,E,I,O,U) to find the character of vowels. 
# if vowels present in strings like a,e,i,o,u not into capital then we have define the
# function to give output is TRUE or else false.



vowel_array = ['a', 'e', 'i', 'o', 'u']


def check_vowel_in_string(stri):
    if vowel_array in stri:
        print("entered string has vowel in it")
    else:
        print("entered string has no vowel in it")


        