 import json as json
from difflib import get_close_matches

'''
OOP Based Dictionary
'''

class dictionary:

    def __init__(self, word):
        self.file_dir = '.\\app1\\data.json'
        self.data = json.load(open(self.file_dir))
        self.dic_word_list = list(self.data.keys())
        self.word = word.lower()

    # Word Finder

    def word_finder(self):

        a = self.word in self.dic_word_list

        if a:
            return a
        else:
            return False

    def word_suggest(self):

        if self.word_finder():
            pass
        else:
            n = get_close_matches(self.word, self.dic_word_list, n=1)
            if len(n) > 0:
                return n[0]
            else:
                return None

    def translator(self):

        if self.word_finder():
            print(self.data[self.word][0])
        else:
            sgt_word = self.word_suggest()
            if sgt_word == None:
                print("The dictionary does not contain the word you typed")
            else:
                YN = input("Did you mean %s instead? Enter Y if yes, or N if no." % sgt_word)
                if YN == 'Y':
                    print(self.data[sgt_word][0])
                else:
                    print("Bye~")


# you_word = input("Enter Word: ")
# dictionary(you_word).translator()
dictionary('cat').translator()
dictionary('cax').word_suggest()
dictionary('ccccc').translator()
dictionary('Cat').translator()
dictionary('Cax').translator()








