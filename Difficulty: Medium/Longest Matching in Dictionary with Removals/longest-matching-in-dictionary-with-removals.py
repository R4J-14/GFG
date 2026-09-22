class Solution:
    def findLongestWord(self, s: str, d: list[str]) -> str:
        # Sort words: primary key by length descending (-len(w)), secondary key alphabetically (w)
        d.sort(key=lambda w: (-len(w), w))

        def is_subsequence(word: str, s: str) -> bool:
            i, j = 0, 0
            len_word, len_s = len(word), len(s)

            while i < len_word and j < len_s:
                if word[i] == s[j]:
                    i += 1
                j += 1

            return i == len_word

        # Return the first matching word
        for word in d:
            if is_subsequence(word, s):
                return word

        return ""