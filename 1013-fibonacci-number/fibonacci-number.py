class Solution:
    def fib(self, n: int) -> int:
        o=1
        t=1
        if n<2:
            return n
        for i in range(2,n):
            t,o=o+t,t
        return t