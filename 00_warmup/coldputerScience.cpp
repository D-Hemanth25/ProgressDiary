#include <iostream>
#include <vector>

int main()
{
    int n;
    std::cin >> n;

    std::vector<int> temperatures(n);
    for (int i = 0; i != n; i++)
    {
        std::cin >> temperatures[i];
    }

    int count { 0 };

    for (auto it: temperatures)
    {
        if (it < 0)
        {
            count++;
        }
    }
    std::cout << count << "\n";
    return 0;
}