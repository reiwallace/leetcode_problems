class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n = 0
        m = 0
        oneNum = "0"
        twoNum = "0"
        for i in range(max(len(version1), len(version2))): 
            while len(version1) > n and version1[n] != ".":
                if oneNum == "0" and version1[n] == "0":
                    n += 1
                    continue
                elif oneNum == "0":
                    oneNum = str(version1[n])
                else:
                    oneNum += str(version1[n])
                n += 1

            while len(version2) > m and version2[m] != ".":
                if twoNum == "0" and version2[m] == "0":
                    m += 1
                    continue
                elif twoNum == "0":
                    twoNum = str(version2[m])
                else:
                    twoNum += str(version2[m])
                m += 1
                
            print(oneNum)
            print(twoNum)

            if int(oneNum) > int(twoNum):
                return 1
            elif int(oneNum) < int(twoNum):
                return -1
            
            n += 1
            m += 1
            if len(version1) > n: oneNum = "0"
            if len(version2) > m: twoNum = "0"

        return 0