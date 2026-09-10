class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        balance = gas[0]
        start = 0
        for i in range(len(cost)):
            balance -= cost[i]
            if balance < 0:
                start = i + 1
                balance = gas[i+1]
                continue
            if i != len(cost) - 1:
                balance += gas[i + 1]
            else:
                balance += gas[0]
        return start