class Solution(object):
    def customSortString(self, order, s):
        mp = defaultdict(int)

        for i in s:
            mp[i] += 1

        ans = ""
        for i in order:
            if i in mp:
                ans += i * mp[i]
                mp[i] = 0

        for key, value in mp.items():
            if value != 0:
                ans += key * value

        return ans