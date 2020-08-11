"""
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the 
input string. The input string can be assumed to contain only alphabets (both 
uppercase and lowercase) and numeric digits.
"""

def duplicate_count(text):
    text_dict = {}
    for i in text.lower():
        text_dict[i] = 1 if i not in text_dict else text_dict[i] + 1
    return len([i for i in text_dict.values() if i > 1])

print(duplicate_count("abcde")) # 0 no characters repeats more than once
print(duplicate_count("aabbcde")) # 2 'a' and 'b'
print(duplicate_count("aabBcde")) # 2 'a' occurs twice and 'b' twice ('b' and 'B')
print(duplicate_count("indivisibility")) # 1 'i' occurs six times
print(duplicate_count("Indivisibilities")) # 2 'i' occurs seven times and 's' occurs twice
print(duplicate_count("aA11")) # 2 'a' and '1'
print(duplicate_count("ABBA")) # 2 'A' and 'B' each occur twice