"""
Shares one letter

Given a list of words, return a dictionary of each unique word as a key and
a list of all the words that share at least one letter (no repetitions) as the
value.
"""

def share_one_letter(wordList):
    wordList = set(wordList)
    d = {}
    for word in wordList:
        d[word] = [w for w in wordList if len(set(word).intersection(w)) != 0]
    return d

print(share_one_letter(['I','say','what','I','mean','and','I','mean','what','I','say']))