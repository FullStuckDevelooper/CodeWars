def anagrams(word, words):
    a =[]
    for x in words:
         if ((sorted(word)) == (sorted(x))):
             a.append(x)
    return a