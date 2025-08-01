class Student: # برای ذخیره اطلاعات هر دانش آموز
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class Classroom: # برای مدیریت لیست دانش‌آموزان و انجام عملیات مختلف روی آن‌ها
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def get_class_average(self):
        if not self.students:
            return 0
        total_grade = 0
        student_count = 0
        for s in self.students:
            if s.grades:
                total_grade += s.get_average_grade()
                student_count += 1
        return total_grade / student_count if student_count > 0 else 0

    def get_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average_grade())

    def get_students_sorted_by_name(self):
        return sorted(self.students, key=lambda s: s.name)
