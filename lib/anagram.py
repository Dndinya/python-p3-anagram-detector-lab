from collections import Counter
class Anagram:
    def __init__(self, word):
        self.word_counts = Counter(word)
        # self.match = match
        
    def match(self, possible_anagrams):
        match = []
        for anagram in possible_anagrams:
            if Counter(anagram) == self.word_counts:
                match.append(anagram)
        return match
                