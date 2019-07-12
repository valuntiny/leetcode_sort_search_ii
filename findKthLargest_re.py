'''
Quest:
    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Example 1:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

    Example 2:
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

    Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.

Solution:
    - should I sort it first?
    - use the idea of quick sort
        but during choose the partition, we only need to keep the half contains the target one
        also we need to sort from highest to lowest
'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p = self.partition(nums)
        if p + 1 > k:
            return self.findKthLargest(nums[:p], k)
        elif p + 1 < k:
            return self.findKthLargest(nums[p + 1:], k - p - 1)
        else:
            return nums[p]


    def partition(self, nums):
        n = len(nums) - 1
        pivot = nums[n]
        i = 0 # index for larger numbers
        for j in range(n):
            if nums[j] >= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[n] = nums[n], nums[i]
        return i


test = Solution()
nums = [3,2,1,5,4,6]
k = 2
print(test.findKthLargest(nums, k))