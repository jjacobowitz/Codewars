"""
Where my anagrams at?

What is an anagram? Well, two words are anagrams of each other if they both 
contain the same letters. 

For example:
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You 
will be given two inputs a word and an array with words. You should return an 
array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) 
=> ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

# Tests
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) # ['aabb', 'bbaa']
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 
                         'racer'])) # ['carer', 'racer']
print(anagrams('laser', ['lazing', 'lazy',  'lacer'])) # []
print(anagrams('a', ['a', 'b', 'c', 'd'])) # ['a']
print(anagrams('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 
                      'racer'])) # ['ab', 'ba']
print(anagrams('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 
                        'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 
                        'babaa'])) # ['aabb', 'bbaa', 'abab', 'baba', 'baab']
print(anagrams('big', ['gig', 'dib', 'bid', 'biig'])) # []