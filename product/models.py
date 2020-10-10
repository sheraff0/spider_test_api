import uuid
# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Название категории')
    external_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='Внешний ID')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Название компании')
    is_active = models.BooleanField(
        default=True, verbose_name='Отображать')
    external_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='Внешний ID')
    location = models.PointField(
        null=True, blank=True,
        srid=4326,
        verbose_name="Местонахождение, координаты"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Название продукта')
    description = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Описание продукта')
    category = models.ForeignKey(
            Category,
            on_delete=models.SET_NULL, null=True,
            verbose_name='Категория',
            related_name='product_category',
            default=None,
        )
    company = models.ForeignKey(
            Company,
            on_delete=models.SET_NULL, null=True,
            verbose_name='Компания',
            related_name='product_company',
            default=None,
        )
    is_active = models.BooleanField(
        default=True, verbose_name='Отображать')
    external_id = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='Внешний ID')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
