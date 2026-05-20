class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            summ = target - nums[i]
            if summ in map:
                return[map[summ],i]
            map[nums[i]] = i
