nums = [2, 3, 4, 5]


def product_array_without_current_element(nums):
    n = len(nums)
    print(n)
    res = [1] * n
    print(res)
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    print(res)
    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] = res[i] * right_product
        right_product = right_product * nums[i]
    return res


print(product_array_without_current_element(nums))
