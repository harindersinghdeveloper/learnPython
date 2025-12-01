#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Example:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


nums = [2,7,11,15,4]
target = 16

#solution1
def returnIndexList1(nums, target):
    indexList = []
    for num in nums:
        diff = target - num
        if diff in nums:
            indexList.append(nums.index(num))
            indexList.append(nums.index(diff))
            return indexList
    if not indexList:
        return "expected numbers not found"

#solution2
def returnIndexList2(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num]=i
    return "expected numbers not found"

print(returnIndexList2(nums, target))


