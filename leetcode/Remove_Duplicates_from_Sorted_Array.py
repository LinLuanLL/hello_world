def removeDuplicates(nums):
    j = 0
    a = len(nums)
    for i in xrange(a):
        if nums[i-j] in nums[i-j+1:]:
            del nums[i-j]
            j += 1
    print(nums)
    return len(nums)

def removeDuplicates2(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

nums = [1,1,1,1,2,5,8,8,9]
a = removeDuplicates2(nums)
print(a)

