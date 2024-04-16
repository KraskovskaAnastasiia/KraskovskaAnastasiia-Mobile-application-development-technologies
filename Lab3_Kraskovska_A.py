class User:
    def __init__(self, name, address, phone_number, age):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.age = age
        self.roles = set()

    def add_role(self, role):
        self.roles.add(role)

    def has_role(self, role):
        return role in self.roles

class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def has_permission(self, permission):
        return permission in self.permissions

# Створення користувачів
user1 = User("Антон", "вул. Великодня, 35", "+123456789", 35)
user2 = User("Анастасія", "вул. Крутецька, 8", "+987654321", 25)

# Створення ролей
teacher_role = Role("Викладач")
teacher_role.add_permission("ставити оцінки")
teacher_role.add_permission("давати завдання")
teacher_role.add_permission("відмічати присутніх")
teacher_role.add_permission("розповідати лекційний матеріал")
teacher_role.add_permission("жартувати")
teacher_role.add_permission("відраховувати студентів")

student_role = Role("Студентка")
student_role.add_permission("здавати лабораторні роботи")
student_role.add_permission("задавати питання")
student_role.add_permission("пропонувати тему для публікації тез")

# Надання ролей користувачам
user1.add_role(teacher_role)
user2.add_role(student_role)

# Перевірка повноважень користувачів
if user1.has_role(teacher_role):
    print(f"{user1.name} має привілегії викладача")
    if teacher_role.has_permission("відмічати присутніх"):
        print(f"{user1.name} може відмічати присутніх студентів на парі")

if user2.has_role(student_role):
    print(f"{user2.name} має привілегії студентки")
    if student_role.has_permission("пропонувати тему для публікації тез"):
        print(f"{user2.name} може пропонувати тему для подальшої публікації тез  :) ")