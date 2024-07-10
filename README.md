# Задание
1. Создать веб-приложение, с API интерфейсом и админ-панелью.
2. Создать базу данных используя миграции Django.

# Технические требования:
* Python 3.8+
* Django 3+
* DRF 3.10+
* PostgreSQL 10+

# Требования к реализации:

**1.** Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из 3 уровней:

* Завод;
* Розничная сеть;
* Индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования 
(не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии 
определяется не названием звена, а отношением к остальным элементам сети, 
т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, 
минуя остальные звенья - её уровень - 1.

**2.** Сделать вывод в админ-панели созданных объектов.

**3.** На странице объекта сети добавить:
* ссылку на «Поставщика»;
* фильтр по названию города;
* «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

**4.** Используя DRF, создать набор представлений:
* CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»);
* Добавить возможность фильтрации объектов по определенной стране.
* Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.


# Для запуска проекта необходимо выполнить следующие действия:

**1.** Установите зависимости из файла requirements.txt

* ### `pip install -r requirements.txt`

**2.** Заполните пустые поля файла .env (образец в файле .env.sample)

**3.** создайте БД

**4.** Примените миграции:
* ### `python manage.py migrate`

**5.** Загрузить тестовые данные командой: python manage.py loaddata data.json

**6.** Запустить приложение

* ### `python manage.py runserver`
