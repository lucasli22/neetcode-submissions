class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        numzeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numzeroes += 1
                continue
            
            product *= nums[i]
        if numzeroes > 1:
            return [0] * len(nums)
        
        answer = list()

        for i in range(len(nums)):
            if nums[i] == 0:
                answer.append(product)
            elif numzeroes > 0:
                answer.append(0)
            else:
                answer.append(product // nums[i])

        return answer