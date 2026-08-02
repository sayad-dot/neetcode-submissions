class Solution:
    def canAttendMeetings(self, intervals):

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):

            previous = intervals[i-1]
            current = intervals[i]

            if previous.end > current.start:
                return False

        return True