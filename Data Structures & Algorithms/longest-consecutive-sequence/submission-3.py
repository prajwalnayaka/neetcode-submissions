class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums) 
        consec_len=1
        for num in nums_set:
            if num-1 not in nums_set:
                length=1
                for i in range(1,len(nums)+1):
                    if num+i in nums_set:
                        length+=1
                    else: break
                if length>consec_len: consec_len=length
        if len(nums)>0:
            return consec_len
        else: return 0