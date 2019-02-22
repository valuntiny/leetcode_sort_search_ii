'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        mid = l + (r - l) // 2

        while l <= r:
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

        return -1

test = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(test.search(nums, target))