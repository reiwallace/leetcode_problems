class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i] > 0 or nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[k] < 0 or nums[i] + nums[j] > 0:
                    break
                total = nums[i] + nums[j] + nums[k]
                if total == 0 and triplets.count([nums[i], nums[j], nums[k]]) < 1:
                    triplets.append([nums[i], nums[j], nums[k]])

                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return triplets 