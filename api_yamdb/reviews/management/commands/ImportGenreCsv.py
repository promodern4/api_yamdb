import csv, os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Genre


class Command(BaseCommand):
    help = 'Импорт данных из csv в модель Genre'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.CSV_FILES_DIR, 'genre.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            objs = [
                Genre(
                    id=row[0],
                    name=row[1],
                    slug=row[2],
                )
                for row in reader
            ]
            Genre.objects.bulk_create(objs)