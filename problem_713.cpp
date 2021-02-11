#include <vector>
#include <string>
#include <iostream>

std::string shortestStandardisedPath(const std::string &path);
void tester(const std::string &path, const std::string &expected);

int main()
{
    std::string testPath = "/usr/bin/../bin/./scripts/../";
    std::string expected = "/usr/bin/";
    tester(testPath, expected);

    testPath = "/myname/documents/../downloads/../desktop/data/";
    expected = "/myname/desktop/data/";
    tester(testPath, expected);

    return 0;
}

void tester(const std::string &path, const std::string &expected)
{
    std::cout << "Path: " << path << " has standardised path: " << shortestStandardisedPath(path) << ". Should be " << expected << ".\n";
}

std::string shortestStandardisedPath(const std::string &path)
{
    std::vector<std::string> pathComponents;
    std::string tempString = "";
    for (const char chr: path)
    {
        if (chr == '/')
        {
            if (tempString == "..")
            {
                pathComponents.pop_back();
            }
            else if (tempString == ".")
            {
                //Nothing
            }
            else
            {
                pathComponents.emplace_back(tempString);
            }
            tempString = "";
        }
        else
        {
            tempString += chr;
        }
    }

    std::string standardPath = "";
    for (const std::string comp : pathComponents)
    {
        standardPath += comp;
        standardPath += "/";
    }
    return standardPath;
}
