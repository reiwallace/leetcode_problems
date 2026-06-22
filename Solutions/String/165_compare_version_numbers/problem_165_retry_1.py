class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1 = version1.split(".")
        split2 = version2.split(".")

        for i in range(len(split1)):
            split1[i] = int(split1[i])

        for i in range(len(split2)):
            split2[i] = int(split2[i])    

        pointer1 = 0
        pointer2 = 0

        while True:
            if (split1[pointer1] > split2[pointer2] and pointer1 == pointer2) or (pointer1 > pointer2 and split1[pointer1] != 0):
                return 1
            elif (split1[pointer1] < split2[pointer2] and pointer1 == pointer2) or (pointer1 < pointer2 and split2[pointer2] != 0):
                return -1
            elif pointer1 == len(split1) - 1 and pointer2 == len(split2) - 1:
                return 0

            if pointer1 < len(split1) - 1:
                pointer1 += 1 
            if pointer2 < len(split2) - 1:
                pointer2 += 1