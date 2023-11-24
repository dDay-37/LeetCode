class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        max_val = max(piles)
        frequencies = [0] * (max_val + 1)

        for balloon in piles:
            frequencies[balloon] += 1

        total_coins = 0
        remaining_chances = len(piles) // 3
        current_turn = 1
        current_number = max_val

        while remaining_chances != 0:
            if frequencies[current_number] > 0:
                if current_turn == 1:
                    current_turn = 0
                else:
                    remaining_chances -= 1
                    current_turn = 1
                    total_coins += current_number
                frequencies[current_number] -= 1
            else:
                current_number -= 1

        return total_coins