class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        if len(hand) % groupSize != 0:
            return False
        
        cntr = Counter(hand)

        hand.sort()
        print(hand)
        for card in hand:
            if card not in cntr:
                continue
            curr = card
            while curr < card + groupSize:
                if curr not in cntr:
                    
                    return False
                cntr[curr] -= 1
                if cntr[curr] == 0:
                    del cntr[curr]
                curr += 1
        return True