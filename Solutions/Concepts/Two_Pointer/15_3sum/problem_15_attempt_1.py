class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i = 0
        triplets = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    break
                j += 1
                k -= 1
                if j == k:
                    total = nums[i] + nums[j - 1] + nums[k]
                    if total == 0:
                        triplets.append([nums[i], nums[j - 1], nums[k]])
                        print("app1")

                    total = nums[i] + nums[j + 1] + nums[k]
                    if total == 0:
                        triplets.append([nums[i], nums[j + 1], nums[k]])
                        print("app2")

        return triplets 
            
            
