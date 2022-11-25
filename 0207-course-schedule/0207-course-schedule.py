class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [[1,0], [2,1], [3,1]] numCourses = 4
        {
            0: [1,0],
            1: [0,1]
        }
        
        prereqs = [[0,1], [0,2], [1,3], [1,4], [3,4]]
        
        {
            0: [1, 2], # []
            1: [3, 4], # []
            2: [],
            3: [4], # []
            4: []
        }
        
        """
        
        # Time O(n * p) where n is number of nodes and p is number of prereqs b/c we have to visit every single node and edge
        # Space O(n * m)
        adj_list = { i:[] for i in range(numCourses) } # {0: [], 1: [0]}
        visited = set() # {  }

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            
            visited.add(course)
            
            for neigh in adj_list[course]:
                if not dfs(neigh):
                    return False
                
            # removes course we have visited already and set it to an empty array b/c we can finish that course so it will return True in case we run dfs on it again
            visited.remove(course) 
            adj_list[course] = []
            return True

        # need to loop through each course in case of graphs that are not connected
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    

        