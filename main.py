class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_number(self):
        for i in self.grades.values():
            average = sum(i) / len(i)
            return average

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_number()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        return result

    def __lt__(self, other):
        if self.average_number() < other:
            print(f"У студента {self.name} средний балл за д/з ниже")
        else:
            print(f"У студента {self.name} средний балл за д/з выше")
        return self.average_number() < other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_number(self):
        for i in self.grades.values():
            average = sum(i) / len(i)
            return average

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_number()}"
        return result

    def __lt__(self, other):
        if self.average_number() < other:
            print(f"У лектора {self.name} средний балл за лекции ниже")
        else:
            print(f"У лектора {self.name} средний балл за лекции выше")
        return self.average_number() < other


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}"
        return result


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'java']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

best_lecturer = Lecturer("Pavel", "Pavlovich")
best_lecturer.courses_attached += ['java']

ordinary_lecturer = Lecturer("Jon", "Jonovich")
ordinary_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

best_student.rate_hw(best_lecturer, 'java', 9)
best_student.rate_hw(best_lecturer, 'java', 10)
best_student.rate_hw(best_lecturer, 'java', 10)

ordinary_student = Student('Lola', 'Lolovna', 'your_gender')
ordinary_student.courses_in_progress += ['Python', 'java']
cool_reviewer.rate_hw(ordinary_student, 'Python', 10)
cool_reviewer.rate_hw(ordinary_student, 'Python', 10)
cool_reviewer.rate_hw(ordinary_student, 'Python', 10)

ordinary_student.rate_hw(ordinary_lecturer, 'Python', 10)
ordinary_student.rate_hw(ordinary_lecturer, 'Python', 8)
ordinary_student.rate_hw(ordinary_lecturer, 'Python', 6)

print(f"{cool_reviewer}\n\n{best_lecturer}\n\n{best_student}")

is_it_lecturer = ordinary_lecturer < best_lecturer.average_number()
is_it_student = ordinary_student < best_student.average_number()
