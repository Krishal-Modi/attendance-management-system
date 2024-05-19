from django.core.management.base import BaseCommand
from student.models import *

class Command(BaseCommand):
    help = 'Delete all students and their attendance records'

    def handle(self, *args, **kwargs):
        StudentAttendanceit.objects.all().delete()
        Studentit.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all students and their attendance records'))