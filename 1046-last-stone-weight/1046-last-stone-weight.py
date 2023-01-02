from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''



        '''
        # Time O(nlogn)
        # Space O(1)
        stones = [x * -1 for x in stones]
        heapify(stones)

        while len(stones) > 1:
            first = heappop(stones) * -1
            second = heappop(stones) * -1
            if second < first:
                new_stone = first - second
                heappush(stones, new_stone * -1)
            
        return stones[0] * -1 if len(stones) else 0