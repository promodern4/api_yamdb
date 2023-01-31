import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import User


class Command(BaseCommand):
    help = 'Импорт данных из csv в модель User'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.CSV_FILES_DIR, 'users.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            objs = [
                User(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    role=row[3],
                    bio=row[4],
                    first_name=row[5],
                    last_name=row[6],
                )
                for row in reader
            ]
            User.objects.bulk_create(objs)
