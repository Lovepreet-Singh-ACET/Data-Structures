class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_yet = max_sum = nums[0]
        for i in nums[1:]:
            max_sum += i
            max_sum = max(max_sum, i)
            max_yet = max(max_sum, max_yet)
        return max_yet
            
