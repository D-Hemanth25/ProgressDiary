import sys

input = sys.stdin.readline
print = sys.stdout.write


def findFirst(numbers, size, target):
    left, right = 0, size - 1
    result = -1
    while left <= right:
        mid = left + ((right - left) // 2)
        if numbers[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result if result != -1 else size


def findLast(numbers, size, target):
    left, right = 0, size - 1
    result = -1
    while left <= right:
        mid = left + ((right - left) // 2)
        if numbers[mid] <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result if result != -1 else -1
 

def main():
    n = int(input())
    numbers = [int(num) for num in input().split()]
    k = int(input())
    queries = []
    for _ in range(k):
        l, r = map(int, input().split())
        queries.append((l, r))

    numbers.sort()
    for query in queries:
        l, r = query
        first, last = findFirst(numbers, n, l), findLast(numbers, n, r)

        if first > last:
            print("0\n")
        else:
            print(f"{last - first + 1} ")
    
main()
