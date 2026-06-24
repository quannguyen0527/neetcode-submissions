class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x in d:
                return [d[x], i]
            else:
                d[nums[i]] = i
        return []