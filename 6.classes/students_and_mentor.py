class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average(self):
        calc = sum([i[1] for i in self.grades]) / len(
            self.grades
        )  # проверить возможно ошибка
        return round(calc, 1)

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}\n\
        Средняя оценка за домашние задания:{self.average()}\n\
        Курсы в процессе изучения:{' '.join(self.courses_in_progress)}\n\
        Завершенные курсы:{' '.join(self.finished_courses)}\n "


class Mentor:
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


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


best_student = Student("Ruoy", "Eman", "your_gender")
best_student.courses_in_progress += ["Python"]

cool_mentor = Mentor("Some", "Buddy")
cool_mentor.courses_attached += ["Python"]

cool_mentor.rate_hw(best_student, "Python", 10)
cool_mentor.rate_hw(best_student, "Python", 10)
cool_mentor.rate_hw(best_student, "Python", 10)

print(best_student.grades)
