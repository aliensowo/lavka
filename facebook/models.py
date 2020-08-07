from django.db import models


class CategoriesProducts(models.Model):
    """Таблица с категориями ФБ товаров/
    Сожержит единственную графу category, в которой хранится название категорий ФБ"""
    category = models.CharField(verbose_name='Категория', name='category', max_length=144)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class ProductFB(models.Model):
    """Единица товара ФБ
    name - наименование товара
    price -цена товара
    count - их количество
    category - связь на таблицу CategoriesProducts, чтобы привязать к конкретной категории
    description - описание товара
    modal - хранит от значение от 1-n, нужна чтобы отслеживать какой товар нажимается"""
    name = models.CharField(verbose_name='Наименование товара', name='name', max_length=144)
    price = models.DecimalField(verbose_name='Цена', name='price', decimal_places=2, max_digits=10)
    count = models.IntegerField(verbose_name='Количество', name='count')
    category = models.ForeignKey(CategoriesProducts, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание', name='description')
    modal = models.CharField(name="modal", max_length=128)
    # добавить строку урлов, в которой будет хранится сами файлы с данными
    # добавить класс таблицу с уралами

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name