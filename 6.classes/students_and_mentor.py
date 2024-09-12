class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_ht(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def calc_average(self):
        val_lst = sum(self.grades.values(), [])
        return round(sum(val_lst) / len(val_lst), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n\
        Средняя оценка за домашние задания: {self.calc_average()}\n\
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n\
        Завершенные курсы: {', '.join(self.finished_courses)}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return self.calc_average() < other.calc_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def calc_average(self):
        val_lst = sum(self.grades.values(), [])
        return round(sum(val_lst) / len(val_lst), 1)

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\n\
        Средняя оценка за лекции: {self.calc_average()}\n"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer\n")
            return
        return self.calc_average() < other.calc_average()


some_student = Student("Ruoy", "Eman", "m")
some_student.courses_in_progress += ["Python", "Git"]
some_student.finished_courses += ["Введение в программирование", "Веб-разработка с нуля"]

du_student = Student("Eva", "Green", "w")
du_student.courses_in_progress += ["Python"]
du_student.finished_courses += ["Введение в программирование", "Веб-разработка с нуля"]

cool_mentor = Reviewer("Some", "Buddy")
some_reviewer = Reviewer("Some", "Buddy")
cool_mentor.courses_attached += ["Python"]

cool_mentor.rate_hw(du_student, "Python", 9)
cool_mentor.rate_hw(du_student, "Python", 8)
cool_mentor.rate_hw(du_student, "Python", 10)

cool_mentor.rate_hw(some_student, "Python", 10)
cool_mentor.rate_hw(some_student, "Python", 9)
cool_mentor.rate_hw(some_student, "Python", 7)

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_in_progress += ["Python"]
some_lecturer.courses_attached += ["Python"]

some_student.rate_ht(some_lecturer, "Python", 7)
some_student.rate_ht(some_lecturer, "Python", 9)
some_student.rate_ht(some_lecturer, "Python", 10)

ser_lecturer = Lecturer("Jastin", "Black")
ser_lecturer.courses_in_progress += ["Python"]
ser_lecturer.courses_attached += ["Python"]

some_student.rate_ht(ser_lecturer, "Python", 9)
some_student.rate_ht(ser_lecturer, "Python", 6)
some_student.rate_ht(ser_lecturer, "Python", 10)

print(some_reviewer)
print(some_lecturer)
print(some_student)
