nums = [1, 4, 5, 6, 8]

print(nums[-2])


class SumbetweenRange:
    def __init__(self, nums):
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sum_range(self, i, j):
        if i == 0:
            return self.prefix_sum[j]
        return self.prefix_sum[j] - self.prefix_sum[i - 1]


s = SumbetweenRange(nums)
print(s.sum_range(2, 4))
