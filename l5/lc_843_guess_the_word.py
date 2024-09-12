import random
from typing import List


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass


class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        attempts = 0  # Track the number of attempts
        match_count = 0  # Track the number of matching letters with the secret word

        # Continue until we either find the secret word or exhaust 10 attempts
        while attempts < 10 and match_count != 6:
            # Randomly select a word from the wordlist to guess
            guess_word = random.choice(wordlist)

            # Get the number of matching letters from the master's guess function
            match_count = master.guess(guess_word)

            # Filter the wordlist to retain only those words that have the same
            # number of matching letters as the guessed word
            new_wordlist = [
                word
                for word in wordlist
                if self.get_matches(guess_word, word) == match_count
            ]

            # Update the wordlist with the narrowed down candidate words
            wordlist = new_wordlist

            # Increment the attempt count
            attempts += 1

    def get_matches(self, word1: str, word2: str) -> int:
        """
        This helper function returns the number of matching characters between
        two words at the same position.
        """
        matches = 0

        # Compare each character at corresponding positions in both words
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                matches += 1

        return matches
