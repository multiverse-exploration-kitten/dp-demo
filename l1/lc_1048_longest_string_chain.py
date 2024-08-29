from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_chain_lengths = {}

        for word in words:
            word_chain_lengths[word] = 1

        longest_chain = 1

        for word in sorted(words, key=len):
            for index in range(len(word)):
                predecessor = word[:index] + word[index + 1:]

                if predecessor in word_chain_lengths:
                    word_chain_lengths[word] = max(
                        word_chain_lengths[word], word_chain_lengths[predecessor] + 1
                    )

            longest_chain = max(longest_chain, word_chain_lengths[word])

        return longest_chain
