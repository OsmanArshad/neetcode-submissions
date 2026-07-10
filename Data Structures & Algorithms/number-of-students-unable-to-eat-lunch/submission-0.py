class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zero_count = students.count(0)
        ones_count = students.count(1)

        for sandwich in sandwiches:
            if sandwich == 0 and zero_count > 0:
                zero_count -= 1
            elif sandwich == 1 and ones_count > 0:
                ones_count -= 1
            else:
                break
        return zero_count + ones_count