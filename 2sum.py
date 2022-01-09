# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         prev = {} #this helps to store the previous elements
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prev:
#                 return [prev[diff], i]
#             prev[n] = i
#         return
# nums = [2,7,11,15 ]   
# target = 9    

# the solution below has a time complexity of O(n^2) and a space complexity of O(0)
def twoSum(array, targetSum):
    for i in range(len(array) -1):
        firstNum = array[i]
    for j in range(i+1, len(array)):
        secondNum = array[j]
    if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]

    return[]
array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
print(twoSum(array,targetSum))

# using hasMap to print 2 sum
# time complexity is O(n) and space complexity is ((1))
# def twoSum(array, targetValues):
#     prev = {}
#     for nums in array:
#         match = targetValues - nums
#         if match in nums:
#             return [targetValues - nums, nums]
#         else:
#             nums[nums] = True
#     return []
# array = [3,5,-4,8,11,1,-1,6]
# targetValues= 10
# print(twoSum(array, targetValues))


#  Using Sorting method
# time complexity is O(nlogn) and space O(n)
# def twoSum(array, targerSum):
#     array.sort()
    
#     left = 0
#     right = len(array) -1
#     while left < right:
#         currentSum = array[left]+ array[right]
#         if currentSum == targerSum:
#             return array[left], array[right]
#         elif currentSum < targerSum:
#             left +=1
#         elif currentSum > targerSum:
#             right -=1
#     return []

# array = [3,5,-4,8,11,1,-1,6]
# targerSum = 10
# print(twoSum(array, targerSum))

         
                