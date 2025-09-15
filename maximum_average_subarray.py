class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #cur_sum = max_sum = sum(nums[:k])
        n = len(nums)
        cur_sum = 0
        for i in range(k):      
            cur_sum += nums[i]
        max_sum = cur_sum

        for i in range(k, n):
            cur_sum += nums[i] - nums[i - k]
            #max_sum = max(max_sum, cur_sum)
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum/k
