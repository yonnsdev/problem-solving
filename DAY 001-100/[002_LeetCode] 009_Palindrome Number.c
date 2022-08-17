#include <stdio.h>
#define bool int

bool isPalindrome(int x);
int main() {
    printf("%d", isPalindrome(-33333));
    return 0;
}

// [Answer]
bool isPalindrome(int x) {
    int y = x;
    int arr[10], i = 0;
    if (x < 0)
        return 0;
    while (y > 0) {
        arr[i] = y % 10;
        y /= 10;
        ;
        i++;
    }
    for (int j = 0; j < i / 2; j++) {
        if (arr[j] == arr[i - j - 1]) {
            continue;
        } else {
            return 0;
        }
    }
    return 1;
}
