'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def searchleft(nums, target):
            left, right = 0, len(nums)-1
            while left < right:
                mid = left + (right - left) // 2 # if there is only two elements left in the [], mid = left
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1

        def searchright(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2 + 1 # if there is only two elements left in the [], mid = right
                if nums[mid] <= target: # this makes the program search for right limit
                    left = mid
                else:
                    right = mid - 1
            return right if nums[right] == target else -1

        return [searchleft(nums, target), searchright(nums, target)]

test = Solution()
nums = [5,7,7,8,8,10]
target = 8
print test.searchRange(nums, target)