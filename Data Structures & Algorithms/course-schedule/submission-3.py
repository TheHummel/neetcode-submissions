class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for p in prerequisites:
            i, j = p
            if i in prereqs:
                prereqs[i].append(j)
            else:
                prereqs[i] = [j]

        visited = set()
        path = set()

        def hasCycle(course):
            if course in path:
                return True

            if course in visited:
                return False


            path.add(course)
            
            
            for prereq in prereqs.get(course, []):
                if hasCycle(prereq):
                    return True

            path.remove(course)
            visited.add(course)

            return False
            
        

        for start in prereqs.keys():
            if hasCycle(start):
                return False    


        return True