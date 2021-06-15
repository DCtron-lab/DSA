class MedianFinder:

    def __init__(self):
        self.maxheap =[]
        self.minheap=[]
        
        heapq.heapify(self.maxheap)
        heapq.heapify(self.minheap)
           

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        
        heapq.heappush(self.minheap,-self.maxheap[0])
        heapq.heappop(self.maxheap)

        if len(self.minheap)>len(self.maxheap):
            heapq.heappush(self.maxheap,-self.minheap[0])   
            heapq.heappop(self.minheap)
        
    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()