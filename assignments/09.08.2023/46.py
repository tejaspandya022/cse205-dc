#Question 46
class Solution(object):
    def permute(self, nums):
        ans=[]
        i=0
        def helper(nums,ans,i):
            if i>=len(nums):
                ans.append(nums[:])
                return 0
            for j in range(i,len(nums)):
                
                nums[i],nums[j]=nums[j],nums[i]
                helper(nums,ans,i+1)
                nums[i],nums[j]=nums[j],nums[i]
        helper(nums,ans,i)
        return ans
