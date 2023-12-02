class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def isPresent(s, q):
            freq = [0] *  256 
            for i in range(0 , len(s)):
                freq[ord(s[i])] += 1
            for i in range(0, len(q)):
                freq[ord(q[i])] -= 1
                if (freq[ord(q[i])] < 0): 
                    return False
            return True
        
        s=0

        for i in words:
            if isPresent(chars,i):
                s+=len(i)
        return s