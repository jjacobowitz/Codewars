"""
Get the Middle Character

You are going to be given a word. Your job is to return the middle character of
the word. If the word's length is odd, return the middle character. If the 
word's length is even, return the middle 2 characters.

#Input
A word (string) of length 0 < str < 1000. You do not need to test for this. 
This is only here to tell you that you do not need to worry about your solution
timing out.
"""

def get_middle(s):
    s_len = len(s)
    return s[(s_len - 1) // 2] if s_len%2==1 else s[(s_len - 1) // 2 : (s_len - 1) // 2 + 2]

print(get_middle("test")) # "es"

print(get_middle("testing")) # "t"

print(get_middle("middle")) # "dd"

print(get_middle("A")) # "A"