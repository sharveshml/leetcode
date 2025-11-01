#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        meetings = []
        
        for i in range(len(start)):
            meetings.append([start[i], end[i]])
        
        meetings.sort(key=lambda x:x[1])
        
        count = 1
        end = meetings[0][1]
        
        for i in range(1, len(meetings)):
            if meetings[i][0] > end:
                count += 1
                end = meetings[i][1]
        
        return count