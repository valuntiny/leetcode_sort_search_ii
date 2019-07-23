'''
Quest:
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

Solution:
    - bisection? search the middle first
        if nums[mid] < target:
'''


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:  # why l <= r instead of l < r?
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  # low - mid dont have pivot
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # low - mid contain pivot
                if nums[mid] <= target <= nums[r]:  # target on left
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

test = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(test.search(nums, target))