nums = [1, 2, 2, 3, 3, 3]
k = 2

freq = {}

for n in nums:
    print(n)
    if n in freq:
        freq[n] = freq[n] + 1
    else:
        freq[n] = 1
sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)


result = []

for i in range(k):
    print(result.append(i))
