
# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        word_chars = [char for char in self.word]
        anagram_words = []
        for word in word_list:
            if sorted(word_chars) == sorted(word):
                anagram_words.append(word)
            else:
                pass
        print(f"anagrams of {self.word}: {anagram_words}")
        return anagram_words

Anagram("enlist").match(["listen", "poison", "hello", "silent"])