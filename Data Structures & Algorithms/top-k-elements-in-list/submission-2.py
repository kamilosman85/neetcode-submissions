class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        out = []
        if len(nums) == 0:
            return []

        for i in nums:
            map[i] = map.get(i,0) + 1

        c = list(map.items())
        for i in range(len(c)):
            for j in range(i+1,len(c)):
                if c[i][1] > c[j][1]:
                    c[i], c[j] = c[j], c[i]
        
        s = c[-k:]
        for q in s:
            out.append(q[0])
        return out
