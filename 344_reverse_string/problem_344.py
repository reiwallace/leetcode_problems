from typing import List
#import math

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for index in range(int(len(s)/2)):
            # Save values on opposite sides of the array
            front_index = s[index]
            back_index = s[-index-1]
            
            # Swap values
            s[index] = back_index
            s[-index-1] = front_index
        return s