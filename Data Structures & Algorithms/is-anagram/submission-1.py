class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for i in s:
            map[i] = map.get(i,0) + 1
        for letter in t:
            map[letter] = map.get(letter,0) - 1
        for a in map.values():
            if a != 0:
                return False
        return True

        