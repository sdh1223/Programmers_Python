#include <iostream>

using namespace std;

int n;
long long fibonacci(int n);

int main() {
	scanf("%d", &n);
	long long f = fibonacci(n);
	printf("%lld", f);
	return 0;
}

long long fibonacci(int n) {
	long long a = 1, b = 1, c = 1;
	if (n == 0) {
		return 0;
	}
	else if (n == 1 || n == 2) {
		return 1;
	}
	else {
		for (int i = 3; i <= n; i++) {
			c = a + b;
			a = b;
			b = c;
		}
		return c;
	}
}

