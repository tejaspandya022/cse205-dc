#Question 39
class Solution(object):
    def combinationSum(self, candidates, target):
       ans=[]
       temp=[]
       def comb(pos,total,temp):
           if total==target:
               ans.append(temp[:])
               return 0
           if total>target:
                return 0   
           for i in range(pos,len(candidates)):
               temp.append(candidates[i])
               comb(i,total+candidates[i],temp)
               temp.pop()

       comb(0,0,temp)
       return ans
