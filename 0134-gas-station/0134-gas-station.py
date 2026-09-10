class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        balance = 0
        start = 0
        for i in range(len(cost)):
            balance += gas[i] - cost[i]
            if balance < 0:
                start = i + 1
                balance = 0
        return start