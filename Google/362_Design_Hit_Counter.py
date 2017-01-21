"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""


"""Solution:
    1. this problem can be solved by tracking the most recent 300 timestamps
    2. therefore, we only need list with 300 spots.
    3. for each timestamp, calculate the timestamp%300 as index and update the index
    4. if the timestamp is new, reset the hits. Otherwise, increase the counter
    5. the key idea for this problem is to track timestamps rather than hits
    6. because timestamps is at most 300 but hits can be very large
"""



class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Tip: using constant space to track timestamps
        self.times = [0]*300
        self.hits = [0]*300
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        # Tip: using self.times to track timestamp and self.hits to track hits
        index = timestamp%300
        if self.times[index] == timestamp:
            self.hits[index] += 1
        else:
            self.times[index] = timestamp
            self.hits[index] = 1

        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # Tip: adding the hits that satisfy the condition
        # this data strucutre won't delete the old timestamp unless a new timestamp has same index
        ret = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                ret += self.hits[i]
        return ret
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)







