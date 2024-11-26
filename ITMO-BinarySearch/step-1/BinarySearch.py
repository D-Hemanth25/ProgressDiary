import sys

input = sys.stdin.readline
print = sys.stdout.write

def binarySearch(nums, size, target):
    left, right = 0, size - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return "YES"
    return "NO"

n, _ = [int(num) for num in input().split()]
numbers = [int(num) for num in input().split()]
queries = [int(k) for k in input().split()]

for query in queries:
    print(binarySearch(numbers, n, query) + "\n")