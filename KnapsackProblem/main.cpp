

#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
// #include <json/value.h>

using namespace std;

int knapsackProblem(int **, int);
int knapsackProblemHelper(int **, int, int, int);

int main(int argc, const char * argv[]) {

	string testCases;
	ifstream testCasesFileContent("test_cases.json", ifstream::binary);
	testCasesFileContent >> testCases;
	// if (testCasesFileContent.is_open()) {
	// 	while (getline(testCasesFileContent, line)) {
	// 		cout << line << '\n';
	// 	}
	// 	testCasesFileContent.close();
	// } else {
	// 	cout << "File is NOT open" << endl;
	// }

	cout << testCases;
	
	//This will print the entire json object.

	//The following lines will let you access the indexed objects.
	// cout<<people["Anna"]; //Prints the value for "Anna"
	// cout<<people["ben"]; //Prints the value for "Ben"
	// cout<<people["Anna"]["profession"]; //Prints the value corresponding to "profession" in the json for "Anna"

	// cout<<people["profession"]; //NULL! There is no element with key "profession". Hence a new empty element will be created.

	return 0;
}






