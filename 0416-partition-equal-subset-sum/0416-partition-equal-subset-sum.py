class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        if sum(nums) % 2 != 0:
            return False
        possible_sums = set()
        possible_sums.add(0)
        target = sum(nums) // 2

        for num in nums:
            new_possible_sums = set()
            for psum in possible_sums:
                new_possible_sums.add(psum)
                if num + psum > target:
                    continue
                if num + psum == target:
                    return True
                new_possible_sums.add(num + psum)
            possible_sums = new_possible_sums
        
        return False