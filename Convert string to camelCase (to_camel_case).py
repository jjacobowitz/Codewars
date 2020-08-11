"""
Convert string to camelCase

Complete the method/function so that it converts dash/underscore delimited 
words into camel casing. The first word within the output should be capitalized
only if the original word was capitalized (known as Upper Camel Case, also 
often referred to as Pascal case).
"""

def to_camel_case(text):
    text = text.replace('_', ' ').replace('-', ' ').split()
    return ''.join([i if text.index(i)==0 else i.lower().title() for i in text[0:]])


print(to_camel_case("the-stealth-warrior")) # returns "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior")) # returns "TheStealthWarrior"
print(to_camel_case("")) # returns ""
print(to_camel_case("A-B-C")) # returns "ABC"