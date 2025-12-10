#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int main() {
    cout << "Input: 5 → Output: Factorial = " << factorial(5) << endl;
    cout << "Input: 0 → Output: Factorial = " << factorial(0) << endl;
    return 0;
}