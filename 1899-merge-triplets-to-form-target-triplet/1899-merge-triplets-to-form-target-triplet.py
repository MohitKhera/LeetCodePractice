class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # x, y, z = target
        # found_x = False
        # found_y = False
        # found_z = False
        # for i in triplets:
        #     a, b, c = i
        #     if a > x or b > y or c > z:
        #         continue
        #     if a == x:
        #         found_x = True
        #     if b == y:
        #         found_y = True
        #     if c == z:
        #         found_z = True
        #     if found_x and found_y and found_z:
        #         return True
        # return found_x and found_y and found_z

        x = y = z = False
        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            if x and y and z:
                return True
        return False