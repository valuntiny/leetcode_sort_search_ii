'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        frq = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        for z, v in dict.items():
            if v in frq:
                frq[v].append(z)
            else:
                frq[v] = [z]

        flag1 = len(nums) # representing frq
        flag2 = k # for counting the k most
        while flag2 > 0:
            if flag1 in frq:
                for j in frq[flag1]:
                    res.append(j)
                    flag2 -= 1 # same level doesn't count as 1
            flag1 -= 1

        return res

test = Solution()
nums = [1,2]
k = 2
print test.topKFrequent(nums, k)
