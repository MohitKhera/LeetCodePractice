class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for i in strs:
            count = [0]*26 # a ... z
            for char in i:
                count[ord(char) - ord("a")] += 1
            grouped[tuple(count)].append(i)
        return list(grouped.values())