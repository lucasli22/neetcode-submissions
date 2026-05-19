class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def hasCycle(course: int) -> bool:
            if course in path:
                return True
            path.add(course)

            for i, j in prerequisites:
                if i == course:
                    if hasCycle(j):
                        return True
            return False
        for course, prereq in prerequisites:
            path = set()
            if hasCycle(prereq):
                return False
            
        return True
        
        
        
            
            