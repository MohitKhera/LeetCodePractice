class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for i in s:
            counts[i] = 1 + counts.get(i, 0)
        res = []
        l, r = 0, 0
        while r <= (len(s) - 1):
            curr_frame = set()
            while True:
                counts[s[r]] -= 1
                curr_frame.add(s[r])
                if counts[s[r]] == 0:
                    curr_frame.remove(s[r])
                r += 1
                if not curr_frame:
                    break
            res.append(r-l)
            l = r

        return res