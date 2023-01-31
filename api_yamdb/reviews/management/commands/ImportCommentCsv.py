import csv, os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Comment, Review, User


class Command(BaseCommand):
    help = 'Импорт данных из csv в модель Comment'

    def handle(self, *args, **options):
        file_path = os.path.join(settings.CSV_FILES_DIR, 'comments.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            objs = [
                Comment(
                    id=row[0],
                    review=Review.objects.get(pk=row[1]),
                    text=row[2],
                    author=User.objects.get(pk=row[3]),
                    pub_date=row[4],
                )
                for row in reader
            ]
            Comment.objects.bulk_create(objs)
