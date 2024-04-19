# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_in_meeting = []

        free_rooms = [i for i in range(n)]

        meetings_held = defaultdict(int)
        
        meetings.sort(key = lambda x : x[0])

        for start_time, end_time in meetings:
            while room_in_meeting and room_in_meeting[0][0] <= start_time:
                heappush(free_rooms, heappop(room_in_meeting)[1])
            
            next_finish_time = end_time

            if free_rooms:
                available_room = heappop(free_rooms)

            else:
                finish_time, available_room = heappop(room_in_meeting)
                next_finish_time += finish_time - start_time
                
            heappush(room_in_meeting, (next_finish_time, available_room))
            meetings_held[available_room] += 1
        
        answer = -1
        curr_meetings_held = 0
        for room_number, meetings_count in meetings_held.items():
            if meetings_count > curr_meetings_held:
                curr_meetings_held = meetings_count
                answer = room_number
        
        return answer