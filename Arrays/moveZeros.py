# 74.99 48ms runtime
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] !=0:
                nums[count] = nums[i]
                count +=1
        if count < n:
            nums[count:] = [0]*(n-count)


# 74.99 48ms runtime
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
# 97.83   40ms runtime
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i,j = 0,0
        while(i < length):
            if nums[j] == 0:
                del nums[j]
                nums.append(0)
                i += 1
                continue
            j += 1
            i += 1

