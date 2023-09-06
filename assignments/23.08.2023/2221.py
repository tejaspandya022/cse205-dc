if (n==1):
            return nums[0]
        else:
            newNums = [0]*(n-1)            
            for i in range(0,n-1):
            
                newNums[i] = (nums[i] + nums[i+1]) % 10
                # nums = newNums
            return self.triangularSum(newNums)
        
