"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}
        
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            
            return copy
        
        return dfs(node) if node else None
        
        

#         adj_list = []
        
#         q = collections.deque()
#         q.append(node)
#         visited = set()
#         visited.add(node.val)
        
#         while q:
#             node = q.popleft()
            
#             visited.add(node.val)
            
#             new_node = Node(node.val, node.neighbors)
#             # adj_list[new_node.val] = new_node.neighbors
#             # adj_list.append(new_node.neighbors)
            
#             nei = []
#             for neigh in new_node.neighbors:
#                 nei.append(neigh)
            
#             adj_list.append(nei)
#             for n in new_node.neighbors:
#                 if n.val not in visited:
#                     q.append(n)
#                     visited.add(n.val)
                    
#         return adj_list
        
        
        