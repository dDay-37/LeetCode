class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        result = [0] * N
        deck.sort()
        self.everyOther(deck, result, 0, 0, False)
        return result

    def everyOther(self, deck: List[int], result: List[int], indexInDeck: int, indexInResult: int, skip: bool) -> None:
        N = len(deck)
        if indexInDeck == N:
            return
        while indexInResult < N:
            if result[indexInResult] == 0:
                if not skip:
                    result[indexInResult] = deck[indexInDeck]
                    indexInDeck += 1
                skip = not skip
            indexInResult += 1
        self.everyOther(deck, result, indexInDeck, 0, skip)