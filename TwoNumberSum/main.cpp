
#include <stdio.h>
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;


void printVector(vector<int>);
vector<int> twoNumberSum1(vector<int>, int);
vector<int> twoNumberSum2(vector<int>, int);


// int main(int argc, char*)
int main(int argc, char *argv[])
{
    vector<int> result = twoNumberSum1(vector<int>{3, 5, -4, 8, 11, 1, -1, 6}, 10);
    printVector(result);

    return 0;
}

// Time complexity: O(n)
// Space complexity: O(n)
vector<int> twoNumberSum1(vector<int> array, int targetSum)
{

    unordered_set<int> complements = unordered_set<int>();
    for (auto it = array.begin(); it != array.end(); it++)
    {
        int complement = targetSum - *it;
        if (complements.find(complement) != complements.end())
        {
            return {*it, complement};
        }
        else if (complements.find(*it) == complements.end())
        {
            complements.insert(*it);
        }
    }

    return vector<int>{};
}


// Time complexity:
// Space complexity:
vector<int> twoNumberSum2(vector<int> array, int targetSum)
{
    
    return vector<int>();
}


void printVector(vector<int> v)
{
    string output = "[ ";
    for (auto it = v.begin(); it != v.end(); it++) {
        output += to_string(*it);
        output += ", ";
    }
    output = output.substr(0, output.length()-2);
    output += " ]";
    cout << "Output: " << output << endl;
}


