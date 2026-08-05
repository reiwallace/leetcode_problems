from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        if len(invocations) < 1:
            if n > 1:
                ans = list(range(n))
                ans.remove(k)
                return ans
            else:
                return []
        def addSusMethods(num):
            if num in susMethods:
                return
            susMethods[num] = 1
            if num in invocationMap:
                for method in invocationMap[num]:
                    addSusMethods(method)

        susMethods = {}
        invocationMap = {}
        for invocation in invocations:
            if invocation[0] in invocationMap:
                invocationMap[invocation[0]].append(invocation[1])
            else:
                invocationMap[invocation[0]] = [invocation[1]]

        addSusMethods(k)

        ans = set()
        for i in range(n):
            if i in susMethods:
                continue

            if i in invocationMap:
                for invoked in invocationMap[i]:
                    if invoked in susMethods:
                        return list(range(n))
                    else:
                        ans.add(invoked)

            ans.add(i)

        return list(ans)


        


        
                
