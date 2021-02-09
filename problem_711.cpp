#include <tuple>
#include <vector>
#include <iostream>

double lineFunction(const double &pointY, const double &x1, const double &y1, const double &x2, const double &y2);
bool testPoint(const std::tuple<double, double> &testPoint, const std::vector<std::tuple<double, double>> &polyPoints);

int main()
{
    // Lesson learnt: tuples in cpp are a significant cancer risk.
    auto t = std::make_tuple(1.0, 1.5);
    std::vector<std::tuple<double, double>> polyPoints = 
        {std::make_tuple(1.0, 2.0),
        std::make_tuple(2.0, 0.0), 
        std::make_tuple(-2.0, 0.0)};
    bool test = testPoint(t, polyPoints);
    std::cout << test << " should be 1.\n";

    t = std::make_tuple(10.0, 1.5);
    polyPoints = 
        {std::make_tuple(1.0, 2.0),
        std::make_tuple(2.0, 0.0), 
        std::make_tuple(-2.0, 0.0)};
    test = testPoint(t, polyPoints);
    std::cout << test  << " should be 0.\n";

    t = std::make_tuple(0.0, 0.25);
    polyPoints = 
        {std::make_tuple(1.0, 2.0),
        std::make_tuple(5.0, 10.0),
        std::make_tuple(2.0, 0.0), 
        std::make_tuple(-2.0, 0.0)};
    test = testPoint(t, polyPoints);
    std::cout << test  << " should be 1.\n";

    t = std::make_tuple(99.0, -101.25);
    polyPoints = 
        {std::make_tuple(1.0, 2.0),
        std::make_tuple(5.0, 10.0),
        std::make_tuple(2.0, 0.0), 
        std::make_tuple(-2.0, 0.0)};
    test = testPoint(t, polyPoints);
    std::cout << test  << " should be 0.\n";

    return 0;
}

// y, x position of point, given line between two points Y (vertical line).
double lineFunction(const double &pointY, const double &x1, const double &y1, const double &x2, const double &y2)
{
    double x = 9999.9999;

    if ((y1 < pointY and pointY < y2) or (y2 < pointY and pointY < y1))
    {
        try
        {
            //y = mx + c => x = (y - c) / m
            if ((x2 - x1) == 0.)
            {
                x = x2;
                return x;
            }

            double m = (y2 - y1) / (x2 - x1);
            double c = y1 - (m * x1);

            x = (pointY - c) / m;
        }
        catch(...) {}
    }

    return x;
}

bool testPoint(const std::tuple<double, double> &testPoint, const std::vector<std::tuple<double, double>> &polyPoints)
{
    double pointX = std::get<0>(testPoint);
    double pointY = std::get<1>(testPoint);

    int numLeft = 0;
    int numRight = 0;
    for (int i = 0; i < polyPoints.size() - 1; i++)
    {
        double polyPointX1 = std::get<0>(polyPoints[i]);
        double polyPointY1 = std::get<1>(polyPoints[i]);

        double polyPointX2 = std::get<0>(polyPoints[i+1]);
        double polyPointY2 = std::get<1>(polyPoints[i+1]);

        double expX = lineFunction(pointY, polyPointX1, polyPointY1, polyPointX2, polyPointY2);
        if (expX != 9999.9999)
        {
            if (pointX < expX)
            {
                numLeft++;
            }
            if (pointX > expX)
            {
                numRight++;
            }
        }

    }

    double polyPointX1 = std::get<0>(polyPoints[polyPoints.size() - 1]);
    double polyPointY1 = std::get<1>(polyPoints[polyPoints.size() - 1]);

    double polyPointX2 = std::get<0>(polyPoints[0]);
    double polyPointY2 = std::get<1>(polyPoints[0]);

    double expX = lineFunction(pointY, polyPointX1, polyPointY1, polyPointX2, polyPointY2);

    if (expX != 9999.9999)
    {
        if (pointX < expX)
        {
            numLeft++;
        }
        if (pointX > expX)
        {
            numRight++;
        }
    }

    if (numLeft % 2 != 0 and numRight % 2 != 0)
    {
        return true;
    }
    return false;
}
