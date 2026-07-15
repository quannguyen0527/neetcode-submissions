class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * (n+2)
        R = [1] * (n+2)
        for i in range(1,n+1):
            L[i] = L[i-1] * nums[i-1] 
            R[n-i+1] = nums[n-i] * R[n-i+2]
        return [L[i-1] * R[i+1] for i in range(1,n+1)]