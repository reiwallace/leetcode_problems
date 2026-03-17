#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    for(int i = 0; i < numsSize; i++) {
        if((i > 0 && nums[i] == nums[i - 1]) || (i < numsSize - 1 && nums[i] == nums[i + 1])) {
            nums[i] = 101;
        }
    }
    int nextEmpty = 0;
    for(int i = 0; i < numsSize; i++) {
        if(nums[i] != 101 && i != nextEmpty) {
            nums[nextEmpty] = nums[i];
            nums[i] = 101;
            nextEmpty ++;
        } else if(nums[i] != 101 && i == nextEmpty) {
            nextEmpty ++;
        }
    }
    return nextEmpty == 0 ? 1 : nextEmpty;
}

int main() {
    int nums[] = {1, 2};
    int numsSize = 2;
    removeDuplicates(nums, numsSize);
    return 0;
}