#include <iostream>
using namespace std;

int num;
int target;
int arr[10000];

int main() {
	int start = 0, end = 0, sum = 0, count = 0;

	scanf("%d", &num);
	scanf("%d", &target);
	for (int i = 0; i < num; i++) {
		scanf("%d", &arr[i]);
	}

	while (end <= num) {
		if (sum < target) {
			sum += arr[end];
			end++;
		}
		else if (sum > target) {
			sum -= arr[start];
			start++;
		}
		else {
			sum -= arr[start];
			start++;
			count++;
		}
	}
	printf("%d", count);
	return 0;
}