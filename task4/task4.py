import sys

file_name = sys.argv[1]

with open(file_name) as file:
    strNums = file.read().split('\n')

nums = [int(n) for n in strNums]
minSum = 0
for n in nums:
    minSum += abs(n - nums[0])

for n in range(1, len(nums)):
    curSum = 0
    for m in nums:
        curSum += abs(m - n)
    if minSum > curSum:
        minSum = curSum
print(minSum)