class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def checkChildren(num):
            if not adjacencyTable[num]:
                return True
            if num in visited:
                return False
            visited.add(num)
            for child in adjacencyTable[num]:
                if not checkChildren(child):
                    return False
            visited.remove(num)
            adjacencyTable[num] = []
            return True

        visited = set()
        adjacencyTable = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjacencyTable[course].append(prereq)

        for entry in adjacencyTable:
            if not checkChildren(entry):
                 return False
        return True

        