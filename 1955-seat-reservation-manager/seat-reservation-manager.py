class SeatManager:

    def __init__(self, n):
        self.heap=list(range(1,n+1))

    def reserve(self):
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber):
        heapq.heappush(self.heap,seatNumber)
