import csv, os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Genre, Title, GenreTitle


class Command(BaseCommand):
    help = 'Импорт данных из csv в модель GenreTitle'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.CSV_FILES_DIR, 'genre_title.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            objs = [
                GenreTitle(
                    id=row[0],
                    genre=Genre.objects.get(pk=row[2]),
                    title=Title.objects.get(pk=row[1]),
                )
                for row in reader
            ]
            GenreTitle.objects.bulk_create(objs)
