import csv, os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Title


class Command(BaseCommand):
    help = 'Импорт данных из csv в модель Title'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.CSV_FILES_DIR, 'titles.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            objs = [
                Title(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category=Category.objects.get(pk=row[3]),
                )
                for row in reader
            ]
            Title.objects.bulk_create(objs)
