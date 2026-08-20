class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        cur1=nums[0]
        cur2=nums[1]
        arr1=[nums[0]]
        arr2=[nums[1]]
        for i in range(2, len(nums)):
            if cur1>cur2:
                arr1.append(nums[i])
                cur1=nums[i]
            else:
                arr2.append(nums[i])
                cur2=nums[i]
        return arr1+arr2