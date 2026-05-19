class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if total % 2 != 0:
            return False
        self.status = False

        def rec(n, currSum):
            if n == len(nums):
                return
            
            if currSum + nums[n] > half:
                return
            elif currSum + nums[n] == half:
                self.status = True
                return
            currSum += nums[n] 
            for i in range(n + 1, len(nums)):
                rec(i, currSum)
        
        rec(0, 0)




        return self.status
                