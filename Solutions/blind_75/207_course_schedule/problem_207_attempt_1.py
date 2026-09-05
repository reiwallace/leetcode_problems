class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def checkChildren(num, visited):
            if num not in adjacencyTable or not adjacencyTable[num]:
                return True
            if num in visited:
                return False
            output = True
            visited.add(num)
            for child in adjacencyTable[num]:
                output &= checkChildren(child, visited)
            visited.remove(num)
            adjacencyTable[num] = []
            return output

        visited = set()
        adjacencyTable = {}
        for prereq in prerequisites:
            course = prereq[0]
            pre = prereq[1]
            if course in adjacencyTable:
                adjacencyTable[course].append(pre)
            else:
                adjacencyTable[course] = [pre]

        output = True
        for entry in adjacencyTable:
            output &= checkChildren(entry, visited)
        return output

        