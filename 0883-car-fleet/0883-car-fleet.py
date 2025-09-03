class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs  = [list(pair) for pair in zip(position, speed)]
        reverse_pairs = sorted(pairs, reverse=True)
        for p, s in reverse_pairs:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)