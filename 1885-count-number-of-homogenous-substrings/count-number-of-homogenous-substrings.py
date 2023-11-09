class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(set(s)) == 1:
            return ((len(s)*(len(s)+1))//2)% ((10**9)+7)
        c=0
        i=0
        while i<len(s):
            j=i
            while j<len(s):
                if s[i]==s[j]:
                    c+=1
                    j+=1
                else:
                    # print(s[i:j])
                    c+=((j-i)*(j-i-1))//2
                    i=j-1
                    break   
            i+=1
        # print("c",c)
        return c % ((10**9)+7)