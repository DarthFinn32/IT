from django.db import models

class BinaryMedia(models.Model):
    file_binary = models.ImageField(upload_to='binary_data/%Y/%m/%d', blank=False, verbose_name='Бинарный файл')

    class Meta:
        abstract = True

class TextualData(models.Model):
    text_content = models.TextField(blank=True, verbose_name='Текстовое содержимое')

    class Meta:
        abstract = True

class NavBinary(BinaryMedia):
    heading = models.CharField(max_length=100, verbose_name='Заголовок вакансии')
    menu_item_1 = models.CharField(max_length=25, verbose_name='Первый пункт меню')
    menu_item_2 = models.CharField(max_length=25, verbose_name='Второй пункт меню')
    menu_item_3 = models.CharField(max_length=25, verbose_name='Третий пункт меню')
    menu_item_4 = models.CharField(max_length=25, verbose_name='Четвертый пункт меню')
    menu_item_5 = models.CharField(max_length=25, verbose_name='Пятый пункт меню')
    author_name = models.CharField(max_length=50, verbose_name='Имя автора')

class MainBinary(BinaryMedia):
    job_description = models.TextField(blank=True, verbose_name='Описание профессии')

class RelevanceData(TextualData):
    salary_graph = models.ImageField(upload_to='binary_data/%Y/%m/%d', blank=False, verbose_name='График уровня зарплат по годам')
    vacancy_graph = models.ImageField(upload_to='binary_data/%Y/%m/%d', blank=False, verbose_name='График количества вакансий по годам')

class GeoData(TextualData):
    city_salary_graph = models.ImageField(upload_to='binary_data/%Y/%m/%d', blank=False, verbose_name='График уровня зарплат по городам')
    city_vacancy_graph = models.ImageField(upload_to='binary_data/%Y/%m/%d', blank=False, verbose_name='График доли вакансий по городам')

class SkillData(TextualData):
    table_identifier = models.CharField(max_length=30, verbose_name='Идентификатор таблицы')
    skills_graphic = models.ImageField(upload_to='binary_data/%Y/%m/%d', blank=False, verbose_name='График по навыкам')

class LatestApiVacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок страницы')
    vacancy = models.TextField(blank=False, verbose_name='Вакансия для парсинга', max_length=15)
