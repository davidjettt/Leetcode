from heapq import heapify, heappush, heappop
class KthLargest:
    '''
        k doesn't change
        guaranteed that there will be k ele in list when add func is called
        add func returns k largest element after val has been added

    '''

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest ints
        self.minHeap = nums
        self.k = k
        heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]



        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)