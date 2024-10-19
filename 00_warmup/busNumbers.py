buses = [6, 2, 1, 9, 4, 3, 8, 12, 13, 14]

buses.sort()

n = len(buses)
left = 0

while left < n:
    right = left
    while right + 1 < n and buses[right + 1] == buses[right] + 1:
        right += 1
    
    if right - left >= 2:
        print(buses[left], "--", buses[right])
    else:
        for i in range(left, right + 1):
            print(buses[i])
    left = right + 1
