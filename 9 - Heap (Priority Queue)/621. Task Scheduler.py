from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a maxHeap & a queue
        # don't care about the actual process, foucus on the frequency and len (time)

        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                processingTaskFreq = heapq.heappop(maxHeap) + 1 # e.g -3 -> -2
                if processingTaskFreq < 0:
                    q.append([processingTaskFreq, time + n]) # time + n is the next available time to process the current task
            if q and q[0][1] == time: # push the waiting tasks back to the Max Heap (need to be placed last for (time + n) algo for time)
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time