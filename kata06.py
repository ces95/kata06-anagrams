from collections import Counter

class Kata():


    list = []
    #data = open('wordlist.txt','r+').read()
    data = open('anagrams.txt','r+').read() #Leemos el archivo
    words = data.split()


    def Anagram (words):

        print("\nCantidad de palabras analizadas: " + str(len(set(words))))

        o = 0
        f = o + 1
        a = words[o]
        b= words[f]
        for word in words:
            if(Counter(a) == Counter(b)):
                list.append(word)
                o= o+1
            else:
                return False



    def Cantidades(list):
        count = 0
        for element in list:
            count += len(element)


        print("\nCantidad de conjuntos de anagramas analizadas: " + str(count))


    #print(words)
    Anagram(words)
    Cantidades(list)


if __name__ == '__main__':
    Kata()
