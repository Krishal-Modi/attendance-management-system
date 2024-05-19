from django.core.management.base import BaseCommand
from student.models import Studentee

class Command(BaseCommand):
    help = 'Add students to the database'

    def handle(self, *args, **options):
        # List of student names
        student_names = [
            "William Wilson",
            "Samantha Davis",
            "Logan Garcia",
            "Chloe Martinez",
            "Daniel Brown",
            "Madison Nguyen",
            "Michael Taylor",
            "Emily Anderson",
            "David Rodriguez",
            "Sophie Hernandez",
            "Joseph Thompson",
            "Emma Moore",
            "Christopher Clark",
            "Abigail Lewis",
            "Joshua Green"
        ]

        # Generate roll numbers (e.g., 001, 002, ...)
        roll_numbers = [f'{i:03}' for i in range(1, len(student_names) + 1)]

        # Create Student objects and save them to the database
        for name, roll_number in zip(student_names, roll_numbers):
            Studentee.objects.create(name=name, roll_number=roll_number)

        self.stdout.write(self.style.SUCCESS('Students added successfully'))


# python manage.py add_studentsae