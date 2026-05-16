from ast import List


def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:  # distinto al anterior → es único
                nums[k] = nums[i]
                k += 1
        return k