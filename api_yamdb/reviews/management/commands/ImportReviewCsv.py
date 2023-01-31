import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Title, Review, User


class Command(BaseCommand):
    help = 'Импорт данных из csv в модель Review'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.CSV_FILES_DIR, 'review.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            objs = [
                Review(
                    id=row[0],
                    title=Title.objects.get(pk=row[1]),
                    text=row[2],
                    author=User.objects.get(pk=row[3]),
                    score=row[4],
                    pub_date=row[5],
                )
                for row in reader
            ]
            Review.objects.bulk_create(objs)
