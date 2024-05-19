from django.core.management.base import BaseCommand
from student.models import Studentme

class Command(BaseCommand):
    help = 'Add and update students to the database'

    def handle(self, *args, **options):
        # List of student names
        student_names = [
            "Hannah Clark",
            "Jacob Thompson",
            "Natalie Brooks",
            "Matthew Hughes",
            "Avery Foster",
            "Samuel Ramirez",
            "Lily Torres",
            "Christopher Bell",
            "Aria Murphy",
            "Joshua Reed",
            "Zoe Jenkins",
            "Jackson Coleman",
            "Lillian Howard",
            "Lucas Peterson",
            "Victoria Price",
            "Henry Sanders",
            "Addison Long",
            "Sebastian Ward",
            "Penelope Mitchell",
            "Dylan Bailey"
        ]

        # Generate roll numbers (e.g., 001, 002, ...)
        roll_numbers = [f'{i:03}' for i in range(1, len(student_names) + 1)]

        # Create Student objects and save them to the database
        for name, roll_number in zip(student_names, roll_numbers):
            Studentme.objects.create(name=name, roll_number=roll_number)

        self.stdout.write(self.style.SUCCESS('Students added successfully'))


# python manage.py add_studentsit

# python manage.py add_studentsme


