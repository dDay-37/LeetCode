class Solution:
    def arrayRankTransform(self, A):
        rank = {}
        for a in sorted(A):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, A)