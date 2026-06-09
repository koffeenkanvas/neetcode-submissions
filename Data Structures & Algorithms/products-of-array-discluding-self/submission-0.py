class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[1] * len(nums)
        running = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = running
            running*=nums[i]
        left = [1] * len(nums)
        runl=1
        for j in range(len(nums)):
            left[j]= runl
            runl*= nums[j]
        answer=[1]*len(nums)
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        return answer