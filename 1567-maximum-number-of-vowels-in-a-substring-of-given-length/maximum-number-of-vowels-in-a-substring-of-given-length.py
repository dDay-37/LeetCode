class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a","e","i","o","u"]
        v1=0
        for i in range(k):
            if s[i] in vowels:
                # print(i,s[i])
                v1+=1
        # print("v1",v1)
        # print(s[:k])
        m=v1
        for j in range(k,len(s)):
            v=0
            # print(s[j])
            if s[j-k] in vowels:
                # print("s[j-k]",s[j-k])
                v-=1
            if s[j] in vowels:
                v+=1
            # print("v",v)
            v1=v1+v
            m=max(m,v1)
        return m