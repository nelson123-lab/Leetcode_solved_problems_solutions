class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sorting the number of the num list.
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
"""   
This problem can be solved using a variation of the two-pointer approach. We can first sort the array and then use two nested loops to fix the first 
two elements of the quadruplet. We can then use two pointers to find the remaining two elements such that their sum is equal to the target.
To avoid duplicates, we can skip over elements that are equal to the previous element in the outer loop and the inner loop. We can also skip over 
elements that are greater than the target minus the sum of the first two elements.
"""
