
from collections import Counter, defaultdict

def anagram(words):
    anagrams = defaultdict(list)
    for word in words:
        histogram = tuple(Counter(word).items()) # build a hashable histogram
        anagrams[histogram].append(word)
    return list(anagrams.values())

def Cantidades(list):
    count = 0
    for element in list:
        count += len(element)
    print("\nCantidad de conjuntos de anagramas analizadas: " + str(len(list)))

#keywords = open('anagrams.txt','r+').read().split()
keywords = ("hi", "hello", "bye", "helol", "abc", "cab",
                "bac", "silenced", "licensed", "declines")

print(anagram(keywords))
Cantidades(anagram(keywords))

"""
def load_words(filename='anagrams.txt'):
    with open(filename,'r+') as f:
        for word in f:
            yield word.rstrip()

def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def print_anagrams(word_source):
    d = get_anagrams(word_source)
    for key, anagrams in d.iteritems():
        if len(anagrams) > 1:
            print(key, anagrams)

word_source = load_words()
print_anagrams(word_source)
"""
