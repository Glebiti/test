lecturers_list =[]
students_list =[]

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def avg_grade(self):                 # средняя очценка
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:  #
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    def add_courses(self, course_name):                # добавить пройденный курс студенту
        self.finished_courses.append(course_name)


    def rate_lecturer(self, student, course_name, grade):          #оценка лекторов студентами
        if isinstance(Lecturer, Lecturer) and course_name in self.courses_in_progress \
                and course_name in lecturer.courses_attached and 1 <= grade <= 5:
            lecturee.grade += [grade]
        else:
            return 'Ошибка'

    def __str__(self):               # магический метод __str__
        return f"Имя: {self.name}\n" \
               f"Фамилмя: {self.surname}\n" \
               f"Средняя оценка за лекцию: {round(self.avg_grade(), 2)}\n" \
               f"Курсы в процессе изучения: {', '.join(map(str, self.courses_in_progress))}\n" \
               f"Завершенные курсы: {', '.join(map(str, self.finished_courses))}"

    def __lt__(self, other):                # сравнение студентов по средней оценке за лекции
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):		#создаем дочерний класс Mentor от родительского Mentor
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        lecturers_list.append(self)

    def avg_grade(self):    #метод оценки лектора, аналогичный методу оценки студентов
        overall_grade = 0
        if len(self.grades) > 0:
            for grade in self.grades:
                overall_grade += grade
            return overall_grade / len(self.grades)
        else:
            return 0

    def __lt__(self, other):    #метод сравнения оценок лекторов
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            return "Ошибка"

    def __str__(self):          # магический метод печати
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \


class Reviewer(Mentor):             # создаем дочерний класс Reviewer

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):                  #магический метод str
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avg_grade_all_lecturers(lecturers_list, course_name):
    all_lecturers_avg_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            all_lecturers_avg_grade += lecturer.avg_grade()
            lecturers_count += 1
    if lecturers_count == 0:
        return 'Ошибка'
    return round(all_lecturers_avg_grade / lecturers_count, 2)

def avg_grade_all_students(students_list, course_name):
    all_students_avg_grade = 0
    students_count = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            all_students_avg_grade += student.avg_grade()
            students_count += 1
    if students_count == 0:
        return 'Ошибка'
    return round(all_students_avg_grade / students_count, 2)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в прогрмирование')

bad_student = Student('Иван', 'Иванов', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.add_courses('Введение в прогрмирование')

cool_reviewer = Reviewer("Some", "Buddy")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer = Reviewer("Петр", "Петров")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(bad_student, 'Git', 10)
cool_reviewer.rate_hw(bad_student, 'Git', 10)
cool_reviewer.rate_hw(bad_student, 'Git', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 9)

cool_lecturer = Lecturer('Som', 'Buddy')
cool_lecturer.courses_attached += ['Python']
lecturers_list.append(cool_lecturer)

def_lecturer = Lecturer('Elijah', 'Baley')
def_lecturer.courses_attached += ['Python']
lecturers_list.append(def_lecturer)

best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 10)

bad_student.rate_lecturer(def_lecturer, "Python", 10)
bad_student.rate_lecturer(def_lecturer, "Python", 10)
bad_student.rate_lecturer(def_lecturer, "Python", 9)

print(cool_lecturer)
print()
print(cool_reviewer)
print()
print(best_student)
print()
print(best_student > bad_student)
print(def_lecturer > cool_lecturer)
print(avg_grade_all_lecturers(lecturers_list, 'Python'))
print(avg_grade_all_students(students_list, 'Python'))