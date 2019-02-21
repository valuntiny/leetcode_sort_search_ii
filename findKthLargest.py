'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid
'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p = self.partition(nums, 0, len(nums)-1)
        if k > p+1:
            return self.findKthLargest(nums[p+1:], k-p-1) # k - (p + 1)
        elif k < p+1:
            return self.findKthLargest(nums[:p], k)
        else:
            return nums[p]

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1

        nums[low], nums[r] = nums[r], nums[low]
        return low

test = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(test.findKthLargest(nums, k))