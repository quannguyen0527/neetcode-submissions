class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        start = []
        n = len(nums)
        for num in nums:
            if num not in mp:
                mp[num] = 1
        for num in nums:
            if num-1 not in mp:
                start.append(num)
        res = 0
        print(start)
        for key in start:
            cnt = 0
            for i in range(n):
                if key+i in mp:
                    cnt += 1
                else:
                    break
            print(key, cnt)
            res = max(res, cnt)
        return res