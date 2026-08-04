class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
            
        insert_index = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[insert_index - 2]:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        return insert_index   