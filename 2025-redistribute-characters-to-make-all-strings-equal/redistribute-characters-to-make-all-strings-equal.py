class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        sent=''.join(words)
        each_letter=set(sent)
        for val in each_letter:
            if sent.count(val)%len(words)!=0:
                return False
        return True