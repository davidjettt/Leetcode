from math import sqrt
from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        k represents how many coords return
        must return answer in order they appear in points


        iterate through points arr and calculate distance to origin for each one and append to aux arr
        heapify the aux array to minHeap
        pop from minHeap k number of times and put that into result array
        return result

        '''
        # Time O(kn)
        # Space O(n)
        distances = []
        for x, y in points:
            distance = sqrt((x  - 0)**2 + (y - 0)**2)
            distances.append([distance, x, y])
        
        heapify(distances)

        res = []
        while k > 0:
            distance, x, y = heappop(distances)
            res.append([x, y])
            k -= 1

        return res


        