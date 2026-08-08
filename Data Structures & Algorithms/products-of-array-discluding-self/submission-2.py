class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        product = []


        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
                postfix.append(nums[len(nums) - 1])
            else:
                prefix.append(nums[i] * prefix[i - 1])
                postfix.append(nums[len(nums) - 1 - i] * postfix[i - 1])
       
        postfix = postfix[::-1]

        for i in range(len(nums)):
            if i == 0:
                product.append(postfix[i + 1])
            elif i == len(nums) - 1:
                product.append(prefix[i - 1])
            else:
                product.append(prefix[i - 1] * postfix[i + 1])
       
        return product
