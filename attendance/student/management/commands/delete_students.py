from django.core.management.base import BaseCommand
from student.models import Student, StudentAttendance

class Command(BaseCommand):
    help = 'Delete all students and their attendance records'

    def handle(self, *args, **kwargs):
        StudentAttendance.objects.all().delete()
        Student.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all students and their attendance records'))


# python manage.py delete_students