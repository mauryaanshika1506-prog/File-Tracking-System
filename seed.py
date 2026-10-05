 import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ftsproject.settings')
django.setup()

from mainapp.models import LoginInfo, Department, Employee

# 1. Admin Account
LoginInfo.objects.get_or_create(
    username='admin@gmail.com', 
    defaults={'password': 'admin@123', 'usertype': 'admin'}
)

# 2. Department Create Karein
dept, _ = Department.objects.get_or_create(dept_name='General')

# 3. Employee 1 Account & Profile
log1, _ = LoginInfo.objects.get_or_create(
    username='emp1@gmail.com', 
    defaults={'password': '87654321', 'usertype': 'employee'}
)
Employee.objects.get_or_create(
    log=log1,
    defaults={
        'empid': 'EMP001',
        'name': 'Employee One',
        'contactno': '9876543210',
        'email': 'emp1@gmail.com',
        'designation': 'Executive',
        'department': dept,
        'address': 'Office Address'
    }
)

# 4. Employee 2 Account & Profile
log2, _ = LoginInfo.objects.get_or_create(
    username='emp2@gmail.com', 
    defaults={'password': '87654321', 'usertype': 'employee'}
)
Employee.objects.get_or_create(
    log=log2,
    defaults={
        'empid': 'EMP002',
        'name': 'Employee Two',
        'contactno': '9876543211',
        'email': 'emp2@gmail.com',
        'designation': 'Assistant',
        'department': dept,
        'address': 'Office Address'
    }
)

print("Database seeded with Admin, Departments, and Employees successfully!")