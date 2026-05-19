class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        path = set()
        self.invalid = False
        ans = []
        preMap = {i: [] for i in range(numCourses)}

        def dfs(course: int):
            if course in path:
                self.invalid = True
                return
            if course in visited:
                return 
            path.add(course)
            
    
            if not preMap[course]:
                ans.append(course)
                visited.add(course)
                path.remove(course)
                return
            
            for crs in preMap[course]:
                dfs(crs) 
                if self.invalid:
                    return
            visited.add(course)
            path.remove(course)
            ans.append(course)
            
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # print(preMap)
        for crs in range(numCourses):
            dfs(crs)
        
        if self.invalid:
            return []
        return ans
            