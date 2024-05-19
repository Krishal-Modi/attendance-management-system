from django.core.management.base import BaseCommand
from student.models import Student

class Command(BaseCommand):
    help = 'Add students to the database'

    def handle(self, *args, **options):
        # List of student names
        student_names = [
            "John Doe",
            "Jane Smith",
            "Alice Johnson",
            "Krishal Modi",
            "Aayush Panchal",
            "Heli Parmar",
            "Rohit Patel",
            "Rajesh Kumar",
            "Jhanvi Shah",
            "Kaushik Dutt",
            "Maharshi Patel",
            "Viranshul Panchal",
            "Aditya Kaushik",
            "Jainam Patel",
            "Adit Panchal",
            "Aniket Shah",
            "Dev Jain",
            "Romil Modi",
            "Sania PanchaL",
            "Vishwajeet Muthe",
            "Vansh Mehta",
            "Rajesh Kumar",
            "Anaf Master",
            "Kalp Mehta",
            "Devendra Gohil",
            "Kabir Ajmeri",
            "Raj Patel",
            "Rajesh Patel",
            "Rajesh Kumar",
        ]

        # Generate roll numbers (e.g., 001, 002, ...)
        roll_numbers = [f'{i:03}' for i in range(1, len(student_names) + 1)]

        # Create Student objects and save them to the database
        for name, roll_number in zip(student_names, roll_numbers):
            Student.objects.create(name=name, roll_number=roll_number)

        self.stdout.write(self.style.SUCCESS('Students added successfully'))


# python manage.py add_students