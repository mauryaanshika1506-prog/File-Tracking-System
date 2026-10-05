import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ftsproject.settings')
django.setup()

from mainapp.models import LoginInfo

# Admin and Employee accounts insert
LoginInfo.objects.get_or_create(
    username='admin@gmail.com', 
    defaults={'password': 'admin@123', 'usertype': 'admin'}
)
LoginInfo.objects.get_or_create(
    username='emp1@gmail.com', 
    defaults={'password': '87654321', 'usertype': 'employee'}
)
LoginInfo.objects.get_or_create(
    username='emp2@gmail.com', 
    defaults={'password': '87654321', 'usertype': 'employee'}
)

print("Database seeded successfully!")