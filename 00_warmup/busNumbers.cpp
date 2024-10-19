#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int n { };
    std::cin >> n;
    
    std::vector<int> buses(n);
    for (int i = { 0 }; i != n; i++)
    {
        std::cin >> buses[i];
    }

    sort(buses.begin(), buses.end());
    int left = { 0 };
    while (left < n)
    {
        int right = { left };
        
        while (right + 1 < n && buses[right + 1] == buses[right] + 1)
        {
            right++;
        } 
        if (right - left >= 2)
        {
            std::cout << buses[left] << "-" << buses[right];
        }
        else
        {
            for (int i = left; i <= right; i++)
            {
                std::cout << buses[i];
                if (i < right)
                {
                    std::cout << " ";
                }
            }
        }
        left = right + 1;
        if (left < n)
        {
            std::cout << " ";
        }
    } 

    std::cout << "\n";
    return 0;
}