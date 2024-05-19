from django.core.management.base import BaseCommand
from student.models import *

class Command(BaseCommand):
    help = 'Delete all students and their attendance records'

    def handle(self, *args, **kwargs):
        StudentAttendanceae.objects.all().delete()
        Studentae.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all students and their attendance records'))


# python manage.py delete_studentsae