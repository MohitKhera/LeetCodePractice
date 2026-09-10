class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hm = {}
        for i in hand:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        heap_list = list(hm.keys())
        heapq.heapify(heap_list)
        for i in range(len(hand) // groupSize):
            while heap_list and hm[heap_list[0]] == 0:
                heapq.heappop(heap_list)
            min_value = heap_list[0]
            for j in range(groupSize):
                if hm.get(min_value + j) == 0 or hm.get(min_value + j) == None:
                    return False
                hm[min_value + j] -= 1 
        return True