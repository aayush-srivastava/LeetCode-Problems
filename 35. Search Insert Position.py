class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
        if target not in nums:
            l = len(nums)
            for j in range(0, len(nums)):
                if target > nums[-1]:
                    return len(nums) 
                elif target > nums[j]:
                    j += 1
                elif target < nums[j]:
                    return j
