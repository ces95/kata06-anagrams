from collections import Counter,  defaultdict

    #data = open('wordlist.txt','r+').read()
words = open('anagrams.txt','r+').read().split() #Leemos el archivo
print("\nCantidad de palabras analizadas: " + str(len(set(words))))

def Anagram (words):
    anagrams = defaultdict(list)
    for word in words:
        h = tuple(Counter(word).items()) # build a hashable histogram
        anagrams[h].append(word)
    return list(anagrams.values())


def Cantidades(list):
    count = 0
    for element in list:
        count += len(element)
    print("\nCantidad de conjuntos de anagramas analizadas: " + str(len(list)))


    #print(words)
Anagram(words)
Cantidades(Anagram(words))
