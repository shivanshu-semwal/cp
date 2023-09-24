class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = [[nums[i], i] for i in range(0, len(nums))]
        items.sort(key=lambda x: x[0])

        left, right = 0, len(items) - 1
        while left < right:
            sum = items[left][0] + items[right][0]
            if sum == target:
                return [items[left][1], items[right][1]]
            
            if sum < target:
                left += 1
            else:
                right -= 1
        
        return None