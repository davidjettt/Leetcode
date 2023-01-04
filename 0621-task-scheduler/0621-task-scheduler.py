import collections
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        tasks is an array of uppercase letters
        tasks[i] represents a task that CPU needs to do
        n = positive integer
        n is cooldown period between 2 same tasks (aka same letter in array)

        tasks can be done in any order
        each task is done in 1 unit of time
        for each unit of time, CPU can finish 1 task or be idle

        being idle still takes up a unit of time

        tasks = ["A","A","A","B","B","B"], n = 2

        


        '''
        # Time O(n * m) where n is size of tasks and m is size of cooldown period
        # Space O(n)
        count = collections.Counter(tasks)
        max_heap = [ -cnt for cnt in count.values() ]
        heapq.heapify(max_heap)

        time = 0
        q = collections.deque() # [count, idleTime]

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(max_heap, cnt)
        
        return time

