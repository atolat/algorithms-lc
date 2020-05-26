## General Patterns

### 2Sum, 3Sum, 4Sum
```python
def threeSum(self, nums):            
    def findPairs(nums, first, target):
        """
        This function will find three numbers that add up to the target
        nums - sorted array
        first - index of the first number 
        target - 3 nums should add up to this number
        """
        start = first + 1
        end = len(nums) - 1
        
        while start < end:
            current_sum = nums[start] + nums[end] + nums[first]
            
            if current_sum == target:
                triplets.append([nums[first], nums[start], nums[end]])
                start += 1
                end -= 1
                # Remember to add these checks to avoid duplicates
                # Keep incrementing start or decrementing end till 
                # there are no duplicates
                while start < end and nums[start] == nums[start-1]:
                    start += 1
                while start < end and nums[end] == nums[end+1]:
                    end -= 1
            elif current_sum < target:
                start += 1
            else:
                end -= 1
                
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        findPairs(nums, i, 0)
        
    return triplets
```