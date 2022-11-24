class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # all pairs of prereq[i] are unique
        # each prereq contains exactly 2 values
        # we need to take prereq[b] before we can take prereq[a]
        
        # numCourses are labeled from 0 to n - 1
        
        #.  
        # [[1,0], [2,1], [3,1]] numCourses = 4
        
        #.   0.      1
        # [[1,0], [0,1]] numCourse = 2
        
        """
        {
            0: [1,0],
            1: [0,1]
        }
        
        
        
        
        """
        
        adj_list = {} # {0: [], 1: [0]}
        visited = set()

        for i in range(numCourses):
            adj_list[i] = []

        for edge1, edge2 in prerequisites:
            adj_list[edge1].append(edge2)


        print(adj_list)
        
        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            
            visited.add(course)
            
            for neigh in adj_list[course]:
                if not dfs(neigh):
                    return False
            visited.remove(course) 
            adj_list[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    

        