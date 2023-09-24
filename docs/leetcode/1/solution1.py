class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        for i in range(0, len(nums)):
            no0 = nums[i]
            no1 = target - no0
            if no1 in items:
                return [i, items[no1]]
            
            items[no0] = i
        
        return None