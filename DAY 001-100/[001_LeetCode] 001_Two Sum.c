#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize);

int main() {
    int nums[4] = {2, 7, 11, 15};
    int returnSize;
    printf("%d", *twoSum(nums, 4, 9, &returnSize));
    return 0;
}

// [Answer]
typedef struct Hashtable {
    int val;
    int idx;
} hashtable;

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    hashtable hash[numsSize];
    int* result = (int*)malloc(sizeof(int) * 2);
    int index = 0;
    do {
        for (int i = 0; i < index; i++) {
            if (hash[i].val == nums[index]) {
                result[0] = index;
                result[1] = hash[i].idx;
                break;
            }
        }
        hash[index].val = target - nums[index];
        hash[index].idx = index;
    } while (++index < numsSize);
    *returnSize = 2;
    return result;
}
