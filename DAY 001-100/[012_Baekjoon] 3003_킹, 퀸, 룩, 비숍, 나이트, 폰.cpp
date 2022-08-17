#include <iostream>

int main() {
    const int pieces[] = {1, 1, 2, 2, 2, 8};
    for (int i = 0; i < 6; i++) {
        int f;
        std::cin >> f;
        std::cout << pieces[i] - f << " ";
    }
    return 0;
}