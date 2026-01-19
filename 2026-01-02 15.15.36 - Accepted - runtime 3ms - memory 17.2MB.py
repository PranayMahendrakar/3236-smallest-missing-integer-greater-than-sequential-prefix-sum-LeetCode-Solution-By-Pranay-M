class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find longest sequential prefix
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefix_sum += nums[i]
            else:
                break
        
        # Find smallest missing integer >= prefix_sum
        nums_set = set(nums)
        result = prefix_sum
        while result in nums_set:
            result += 1
        return result