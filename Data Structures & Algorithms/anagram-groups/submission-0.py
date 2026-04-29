class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for i in strs:
            c = "".join(sorted(i))
            map[c] = map.get(c,[]) + [i]
        return list(map.values())
