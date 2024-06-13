class Solution(object):
    def minMovesToSeat(self, seats, students):
        max_position = 100
        seat_count = [0] * (max_position + 1)
        student_count = [0] * (max_position + 1)
        
        for seat in seats:
            seat_count[seat] += 1
        
        for student in students:
            student_count[student] += 1
        
        seat_idx = 0
        student_idx = 0
        moves = 0
        
        while seat_idx <= max_position and student_idx <= max_position:
            while seat_idx <= max_position and seat_count[seat_idx] == 0:
                seat_idx += 1
            while student_idx <= max_position and student_count[student_idx] == 0:
                student_idx += 1
            
            if seat_idx <= max_position and student_idx <= max_position:
                count = min(seat_count[seat_idx], student_count[student_idx])
                moves += count * abs(seat_idx - student_idx)
                seat_count[seat_idx] -= count
                student_count[student_idx] -= count
        
        return moves

        