class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable = len(students)
        
        while sandwiches and unable > 0:
        
            if students[0] == sandwiches[0]:
                unable -= 1
                students.pop(0)
                sandwiches.pop(0)

            else:
                if all(student != sandwiches[0] for student in students):
                    break
                students.append(students[0])
                students.pop(0)

        return unable

