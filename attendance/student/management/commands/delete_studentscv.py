from django.core.management.base import BaseCommand
from student.models import Studentcv, StudentAttendancecv

class Command(BaseCommand):
    help = 'Delete all students and their attendance records'

    def handle(self, *args, **kwargs):
        StudentAttendancecv.objects.all().delete()
        Studentcv.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all students and their attendance records'))


# python manage.py delete_studentscv