class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []


sol = Solution()

print("Test Case 1:", sol.twoSum([2, 7, 11, 15], 9))


print("Test Case 2:", sol.twoSum([3, 2, 4], 6))

print("Test Case 3:", sol.twoSum([3, 3], 6))

print("Test Case 4:", sol.twoSum([-3, 4, 3, 8], 5))

print("Test Case 5:", sol.twoSum([1, 2, 3], 10))
