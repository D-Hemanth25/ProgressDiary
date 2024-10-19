#include <iostream>

int main()
{
    long long x, y;
    
    while (std::cin >> x >> y)
    {
        std::cout << llabs(x - y) << "\n";
    }
    return 0;
}