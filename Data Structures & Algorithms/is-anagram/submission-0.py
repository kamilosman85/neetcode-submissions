class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        if len(s) != len(t):
            return False
        for i in s:
            map[i] = map.get(i,0)+1
        for c in t:
            map[c] = map.get(c,0) - 1 
        for a in map.values():
            if a != 0:
                return False
        return True
        