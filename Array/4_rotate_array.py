class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        ## Method 1:
        # nums = nums[-k:] + nums[:k+1]  
        
        ##Method 2: time - O(N), space - O(N)
        # temp[(i+k)%N] = nums[i]
        # N = len(nums)
        # temp = [0]*N
        # for i in range(N):
        #     temp[(i+k)%N] = nums[i]
        # for i in range(len(nums)):
        #     nums[i] = temp[i]
        
        ##Method 3: time - O(N), space - O(1)
        N = len(nums)
        k = k % N
        
        #Reverse 0 to N-k Array 
        for i in range((N-k)//2):
            temp = nums[i]
            nums[i] = nums[N-k-i-1]
            nums[N-k-i-1] = temp
        
        #Reverse N-k to N Array
        for i in range(N-k,N-k//2):
            temp = nums[i]
            nums[i] = nums[N-k-i-1]
            nums[N-k-i-1] = temp
                  
        #Reverse 0 to N Array
        for i in range(N//2):
            temp = nums[i]
            nums[i] = nums[N-i-1]
            nums[N-i-1] = temp
            
        
