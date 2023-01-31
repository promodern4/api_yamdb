# **Проект api_yamdb**
#### Назначение
Проект *api_yamdb* представляет собой учебный проект, предназначенный для реализации полученных навыков в области *API*
#### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории. Произведению может быть присвоен жанр из списка предустановленных. Добавлять произведения, категории и жанры может только администратор. Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв. Пользователи могут оставлять комментарии к отзывам. Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
### Технологии: 
- Python 3.7 
- Django 3.2 
- Django REST framework 3.12.4 
- PyJWT 2.1.0 
- Pytest 6.2.4 
- Pytest-django 4.4.0 
- Pytest-pythonpath 0.7.3 
- Django-filter 22.1 
- djangorestframework-simplejwt 4.7.2
### Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:
``` 
git clone https://github.com/promodern4/api_yamdb.git 
```
``` 
cd api_yamdb 
``` 
Cоздать и активировать виртуальное окружение: 
``` 
python3 -m venv env 
```
``` 
source venv/bin/activate 
``` 
Установить зависимости из файла requirements.txt: 
``` 
python3 -m pip install --upgrade pip 
``` 
``` 
pip install -r requirements.txt 
```
Выполнить миграции: 
``` 
python3 manage.py migrate 
``` 
Запустить проект: 
``` 
python3 manage.py runserver 
``` 
Документация с примерами запросов и ответов на них по адресу  
``` 
http://127.0.0.1:8000/redoc/ 
``` 
### Примеры запросов 
*Получение списка всех категорий* 
GET
```
http://127.0.0.1:8000/api/v1/categories/ 
``` 
RESPONCE 
```
{ 
  "count": 0, 
  "next": "string", 
  "previous": "string", 
  "results": [ 
    { 
      "name": "string", 
      "slug": "string" 
    } 
  ] 
} 
```

*Добавление произведения* 
POST 
``` 
http://127.0.0.1:8000/api/v1/titles/ 
``` 
PAYLOAD 
``` 
{ 
  "name": "string", 
  "year": 0, 
  "description": "string", 
  "genre": [ 
    "string" 
  ], 
  "category": "string" 
} 
``` 
RESPONCE 
``` 
{ 
  "id": 0, 
  "name": "string", 
  "year": 0, 
  "rating": 0, 
  "description": "string", 
  "genre": [ 
    { 
      "name": "string", 
      "slug": "string" 
    } 
  ], 
  "category": { 
    "name": "string", 
    "slug": "string" 
  } 
} 
```

### Импорт данных
Из дериктории проекта запустите команды импорта:
```
python3 manage.py ImportUsersCsv
```
```
python3 manage.py ImportCategoryCsv
```
```
python3 manage.py ImportGenreCsv
```
```
python3 manage.py ImportTitleCsv
```
```
python3 manage.py ImportGenreTitleCsv
```
```
python3 manage.py ImportReviewCsv
```
```
python3 manage.py ImportCommentCsv
```
