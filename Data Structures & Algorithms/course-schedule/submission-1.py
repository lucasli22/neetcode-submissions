class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        safe = set()
        preMap = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        
        def hasCycle(course: int) -> bool:
            if course in path:
                return True
            if course in safe:
                return False
            path.add(course)

            for crs in preMap[course]:
                    if hasCycle(crs):
                        return True
                    else:
                        safe.add(crs)
            path.remove(course)
            return False
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True
        
        
        
            
            