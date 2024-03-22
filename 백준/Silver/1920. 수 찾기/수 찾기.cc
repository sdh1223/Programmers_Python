#include <iostream>
#include <algorithm>
using namespace std;

int n;
int m;
int arr1[100000];
int arr2[100000];

int main() {

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &arr1[i]);
	}

	scanf("%d", &m);

	for (int i = 0; i < m; i++) {
		scanf("%d", &arr2[i]);
	}

	sort(arr1, arr1 + n);
	
	for (int i = 0; i < m; i++) {

		bool isIn = binary_search(arr1, arr1 + n, arr2[i]);

		if (isIn) {
			printf("%d\n", 1);
		}
		else {
			printf("%d\n", 0);
		}
	}

	return 0;
}