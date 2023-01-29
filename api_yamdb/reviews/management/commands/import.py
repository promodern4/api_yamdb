import csv

from django.core.management import BaseCommand
from reviews.models import (Category, Comment,
                            Genre, GenreTitle,
                            Review, Title, User)


class Command(BaseCommand):

    def handle(self, *args, **options):

        print("Loading users.csv")
        with open('static/data/users.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Пропускаем строчку заголовка
            next(reader)
            for row in reader:
                User(id=row[0],
                     username=row[1],
                     email=row[2],
                     role=row[3],
                     bio=row[4],
                     first_name=row[5],
                     last_name=row[6]).save()

        print("Loading category.csv")
        with open('static/data/category.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Category(id=row[0],
                         name=row[1],
                         slug=row[2]).save()

        print("Loading genre.csv")
        with open('static/data/genre.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                Genre(id=row[0],
                      name=row[1],
                      slug=row[2]).save()

        print("Loading title.csv")
        with open('static/data/titles.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                category = Category.objects.get(id=row[3])
                Title(id=row[0],
                      name=row[1],
                      year=row[2],
                      category=category).save()

        print("Loading genre_title.csv")
        with open('static/data/genre_title.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title_id = Title.objects.get(id=row[1])
                genre_id = Genre.objects.get(id=row[2])
                GenreTitle(id=row[0],
                           title=title_id,
                           genre=genre_id).save()

        print("Loading review.csv")
        with open('static/data/review.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title = Title.objects.get(id=row[1])
                author = User.objects.get(id=row[3])
                Review(id=row[0],
                       title_id=title.id,
                       text=row[2],
                       author=author,
                       score=row[4],
                       pub_date=row[5]).save()

        print("Loading comments.csv")
        with open('static/data/comments.csv', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                review_id = Review.objects.get(id=row[1])
                author = User.objects.get(id=row[3])
                Comment.objects.create(
                    id=row[0],
                    review=review_id,
                    text=row[2],
                    author=author,
                    pub_date=row[4]).save()
