def twoSum(nums, target):
    for i in range(0,len(nums)):
        if target - nums[i] in nums[i+1:]:
            return [i,nums.index(target - nums[i],i+1)]
nums = [2, 7, 11, 15]
target = 9
(a,b) = twoSum(nums,target)
