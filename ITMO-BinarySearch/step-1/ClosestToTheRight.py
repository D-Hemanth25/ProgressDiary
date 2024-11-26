import sys

input = sys.stdin.readline
print = sys.stdout.write


def binarySearch(nums, size, target):
    left, right = 0, size - 1
    result = -1
    while left <= right:
        mid = left + ((right - left) // 2)
        if nums[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result + 1 if result != -1 else size + 1


def main():
    n, _ = [int(num) for num in input().split()]
    numbers = [int(num) for num in input().split()]
    queries = [int(k) for k in input().split()]

    for query in queries:
        print(str(binarySearch(numbers, n, query)) + "\n")


main()