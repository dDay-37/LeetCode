class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_num = bin(n).replace("0b", "")
        reverse_bin = str(bin_num)[::-1]
        reverse_bin += '0'*(32 - len(reverse_bin))
        return int(reverse_bin,2)
