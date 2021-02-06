#include <iostream>
#include <vector>

// This problem was asked by Apple.

// A fixed point in an array is an element whose value is equal to its index. 
// Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
// For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

struct validFixedPoint
{
    int fixedPoint;
    bool valid;
};

void fixedPointTester(const std::vector<int> &pointArr, int expectedValue, bool expectedValid);
validFixedPoint fixedPointCalculator(const std::vector<int> &point);
std::ostream& operator<<(std::ostream& os, const std::vector<int> &input);

int main()
{
    std::vector<int> testArrOne = {-6, 0, 2, 40}; // Should be 2
    std::vector<int> testArrTwo = {1, 5, 7, 8}; // Should be false

    fixedPointTester(testArrOne, 2, true);
    fixedPointTester(testArrTwo, -1, false);



    return 0;
}

void fixedPointTester(const std::vector<int> &pointArr, int expectedValue, bool expectedValid)
{
    validFixedPoint fp = fixedPointCalculator(pointArr);
    int val = fp.fixedPoint;
    bool exists = fp.valid;

    std::cout << "Array: " << pointArr << " Value: " << val << " valid: " << exists 
    << ". Should be: " << expectedValue << ", " << expectedValid << ".\n";
}

validFixedPoint fixedPointCalculator(const std::vector<int> &pointArr)
{
    validFixedPoint fp;
    fp.fixedPoint = -1;
    fp.valid = false;
    
    for (int i = 0; i < pointArr.size(); i++)
    {
        if (i < pointArr.at(i))
        {
            return fp;
        }

        if (i == pointArr.at(i))
        {
            fp.fixedPoint = i;
            fp.valid = true;
            return fp;
        }
    }

    return fp;
}

// Overloading << so that I can easily print out a vector.
std::ostream& operator<<(std::ostream& os, const std::vector<int> &input)
{
    for (auto const& i: input) {
        os << i << " ";
    }
    return os;
}
