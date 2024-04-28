#15. Створити додаток для керування навчальним процесом 
#з класами для курсів, завдань, оцінок та відстеження прогресу студентів.

class Course:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False
    
    def complete(self):
        self.completed = True

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.progress = {}

    def submit_task(self, task_name, completion_status):
        self.progress[task_name] = completion_status

    def get_progress(self):
        return self.progress

class ProgressTracker:
    def __init__(self):
        self.students_progress = {}

    def track_progress(self, student, course, task, completion_status):
        if student.name not in self.students_progress:
            self.students_progress[student.name] = {}
        if course.name not in self.students_progress[student.name]:
            self.students_progress[student.name][course.name] = {}
        self.students_progress[student.name][course.name][task.name] = completion_status

    def get_student_progress(self, student):
        if student.name in self.students_progress:
            return self.students_progress[student.name]
        else:
            return {}

math_course = Course("Математика")
science_course = Course("Комп'ютерні науки")
programming_course = Course("Програмування")
english_course = Course("Англійська мова")
germany_course = Course("Німецька мова")

math_hw = Task("Домашнє завдання з математики", "2024-05-15")
science_project = Task("Проєкт з комп'ютерних наук", "2024-05-20")
programming_hw = Task("Домашнє завдання з програмування", "2024-05-22")
english_hw = Task("Домашнє завдання з англійської", "2024-05-24")
germany_hw = Task("Домашнє завдання з німецької", "2024-05-27")

math_course.add_task(math_hw)
science_course.add_task(science_project)
programming_course.add_task(programming_hw)
english_course.add_task(english_hw)
germany_course.add_task(germany_hw)

student1 = Student("Красковська Анастасія", 10)
student2 = Student("Вуйко Олександр", 9)

progress_tracker = ProgressTracker()

student1.submit_task(math_hw.name, True)
student1.submit_task(science_project.name, False)
student1.submit_task(programming_hw.name, True)
student1.submit_task(english_hw.name, True)
student1.submit_task(germany_hw.name, True)

student2.submit_task(math_hw.name, False)
student2.submit_task(science_project.name, True)
student2.submit_task(programming_hw.name, True)
student2.submit_task(english_hw.name, False)
student2.submit_task(germany_hw.name, True)

# Відстеження прогресу студентів
progress_tracker.track_progress(student1, math_course, math_hw, True)
progress_tracker.track_progress(student1, science_course, science_project, False)
progress_tracker.track_progress(student1, programming_course, programming_hw, True)
progress_tracker.track_progress(student1, english_course, english_hw, True)
progress_tracker.track_progress(student1, germany_course, germany_hw, True)

progress_tracker.track_progress(student2, math_course, math_hw, False)
progress_tracker.track_progress(student2, science_course, science_project, True)
progress_tracker.track_progress(student2, programming_course, programming_hw, True)
progress_tracker.track_progress(student2, english_course, english_hw, False)
progress_tracker.track_progress(student2, germany_course, germany_hw, True)

# Отримання прогресу студентів
print("Прогрес для студента:", student1.name)
print(progress_tracker.get_student_progress(student1))
print("\nПрогрес для студента:", student2.name)
print(progress_tracker.get_student_progress(student2))
