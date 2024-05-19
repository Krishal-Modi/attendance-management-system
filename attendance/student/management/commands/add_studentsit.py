from django.core.management.base import BaseCommand
from student.models import Studentit

class Command(BaseCommand):
    help = 'Add and update students to the database'

    def handle(self, *args, **options):
        # List of student names
        student_names = [
            "Emily Brown",
    "Michael Wilson",
    "Sarah Davis",
    "David Martinez",
    "Laura Garcia",
    "Daniel Rodriguez",
    "Samantha Lee",
    "James Walker",
    "Olivia Hall",
    "Benjamin Young",
    "Emma King",
    "Liam Wright",
    "Mia Scott",
    "William Green",
    "Ava Adams",
    "Ethan Hill",
    "Sophia Baker",
    "Noah Nelson",
    "Isabella Carter",
    "Lucas Rivera",
    "Charlotte Perez",
    "Mason Turner",
    "Amelia Phillips",
    "Logan Roberts",
    "Harper Campbell",
    "Alexander Parker",
    "Evelyn Evans",
    "Elijah Edwards",
    "Abigail Collins",
    "Aiden Stewart",
    "Ella Sanchez",
    "Jack Morris",
    "Grace Rogers"
        ]

        # Generate roll numbers (e.g., 001, 002, ...)
        roll_numbers = [f'{i:03}' for i in range(1, len(student_names) + 1)]

        # Create Student objects and save them to the database
        for name, roll_number in zip(student_names, roll_numbers):
            Studentit.objects.create(name=name, roll_number=roll_number)

        self.stdout.write(self.style.SUCCESS('Students added successfully'))


# python manage.py add_studentsit