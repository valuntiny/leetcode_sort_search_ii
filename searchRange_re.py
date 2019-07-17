'''
Quest:
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
    Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Solution:
    -bi section still?
        yes, but since we are trying to find both end, we need to do it twice, one for beginning, one for ending
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

        def findleft(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2  # when only two elements, mid = l
                if nums[mid] < target:  # [no, yes] ok
                    l = mid + 1
                else:  # [yes, yes] ok, [yes, no] ok
                    r = mid
            return l if nums[l] == target else -1

        def findright(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2 + 1  # when only two elements, mid = r
                if nums[mid] <= target:  # [yes, yes], [no, yes]
                    l = mid
                else:  # [yes, no] ok
                    r = mid - 1
            return l if nums[l] == target else -1

        return [findleft(nums, target), findright(nums, target)]


test = Solution()
nums = [5,7,7,8,8,10]
target = 6
print(test.searchRange(nums, target))
