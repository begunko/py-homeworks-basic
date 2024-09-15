from data import students, reviewers, lecturers


class Student:
    instances = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.instances.append(self)

    def rate_ht(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self) -> str:
        grade = []
        if self.courses_in_progress != []:
            progress = ", ".join(self.courses_in_progress)
        else:
            progress = "курсов в процессе изучения пока нет."
        if self.finished_courses != []:
            finished = ", ".join(self.finished_courses)
        else:
            finished = "завершенных курсов пока нет."
        if self.grades != {}:
            val_lst = sum(self.grades.values(), [])
            if len(val_lst):
                grade = round(sum(val_lst) / len(val_lst), 1)
            else:
                grade = "оценок пока нет."
        else:
            grade = "оценок пока нет."
        return f"Студент:\nИмя: {self.name}\nФамилия: {self.surname}\n\
        Средняя оценка за домашние задания: {grade}\n\
        Курсы в процессе изучения: {progress}\n\
        Завершенные курсы: {finished}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return self.calc_average() < other.calc_average()


class Mentor:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []


class Reviewer(Mentor):
    instances = []

    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        Reviewer.instances.append(self)

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
        return f"Ревьюер:\nИмя: {self.name}\nФамилия: {self.surname}\n"


class Lecturer(Mentor):
    instances = []

    def __init__(self, name, surname, gender):
        super().__init__(name, surname, gender)
        self.courses_in_progress = []
        self.grades = {}
        Lecturer.instances.append(self)

    def __str__(self):
        grade = {}
        if self.grades != {}:
            val_lst = sum(self.grades.values(), [])
            if len(val_lst):
                grade = round(sum(val_lst) / len(val_lst), 1)
            else:
                grade = "оценок пока нет."
        else:
            grade = "оценок пока нет."
        return f"Имя:{self.name}\nФамилия:{self.surname}\n\
        Средняя оценка за лекции: {grade}\n"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer\n")
            return
        return self.calc_average() < other.calc_average()


for i in students:
    Student(i["name"], i["surname"], i["gender"])
    id_stud = students.index(i)
    std = Student.instances[id_stud]
    if "finished_courses" in students[id_stud]:
        std.__dict__["finished_courses"] = i["finished_courses"]
    if "courses_in_progress" in students[id_stud]:
        std.__dict__["courses_in_progress"] = i["courses_in_progress"]
    if "grades" in students[id_stud]:
        std.__dict__["grades"] = i["grades"]


for i in reviewers:
    Reviewer(i["name"], i["surname"], i["gender"])
    id_rew = reviewers.index(i)
    rew = Reviewer.instances[id_rew]
    if "courses_attached" in reviewers[id_rew]:
        rew.__dict__["courses_attached"] = i["courses_attached"]


for i in lecturers:
    Lecturer(i["name"], i["surname"], i["gender"])
    id_lec = lecturers.index(i)
    lec = Lecturer.instances[id_lec]
    if "courses_attached" in lecturers[id_lec]:
        lec.__dict__["courses_attached"] = i["courses_attached"]


# перебор всех студентов
for i in Student.instances:
    print(i.__str__())

# перебор всех ревьюеров
for i in Reviewer.instances:
    print(i.__str__())

# перебор всех лекторов
for i in Lecturer.instances:
    print(i.__str__())
