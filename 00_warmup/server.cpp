#include <iostream>
#include <vector>

int main()
{
    int n { }, t { };
    std::cin >> n >> t;

    std::vector<int> tasks(n);
    for (int i = 0; i != n; i++)
    {
        std::cin >> tasks[i];
    }

    int completed { 0 }, time { 0 };
    for (auto task: tasks)
    {
        if (time + task <= t)
        {
            time += task;
            completed++;
        }
        else
        {
            break;
        }
    }

    std::cout << completed << "\n";
    return 0;
}