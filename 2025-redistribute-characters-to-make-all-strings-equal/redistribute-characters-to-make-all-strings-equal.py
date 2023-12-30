class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charCount = {}
        numWords = len(words)

        for word in words:
            for char in word:
                charCount[char] = charCount.get(char, 0) + 1

        for count in charCount.values():
            if count % numWords != 0:
                return False

        return True