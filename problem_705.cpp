#include <iostream>
#include <vector>


int calcTrappedWater(const std::vector<int> &wall)
{
    bool wallOpened = false;
    bool wallClosed = false;
    int currWall = 0;
    int trappedWater = 0;
    int tempTrappedWater = 0;

    for(int height : wall)
    {
        if (height >= currWall)
        {
            if (wallOpened == false and wallClosed == false)
            {
                wallOpened = true;
                currWall = height;

            }
            else if (wallOpened == true and wallClosed == false)
            {
                wallOpened = false;
                wallClosed = true;
                trappedWater += tempTrappedWater;
                tempTrappedWater = 0;
                currWall = height;
            }
            else if (wallOpened == false and wallClosed == true)
            {
                wallOpened = true;
                wallClosed = false;
                trappedWater += tempTrappedWater;
                tempTrappedWater = 0;
                currWall = height;
            }
        }
        else if (height < currWall)
        {
            tempTrappedWater += currWall - height;
        }
    }
    return trappedWater;
}

int main()
{
    const std::vector<int> wall_simple = {2, 1, 2};
    const std::vector<int> wall_complex_one = {3, 0, 1, 3, 0, 5};
    const std::vector<int> wall_complex_two= {3, 0, 1, 3, 0, 0};
    const std::vector<int> wall_complex_three = {0, 0, 1, 3, 0, 5};

    std::cout << "Trapped water: " << calcTrappedWater(wall_simple) << " Should be 1.\n";
    std::cout << "Trapped water: " << calcTrappedWater(wall_complex_one) << " Should be 8.\n";
    std::cout << "Trapped water: " << calcTrappedWater(wall_complex_two) << " Should be 5.\n";
    std::cout << "Trapped water: " << calcTrappedWater(wall_complex_three) << " Should be 3.\n";

    return 0;
}
