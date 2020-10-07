import uuid
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Описание компании')
    is_active = models.BooleanField(
        default=True, verbose_name='Отображать')

    def __str__(self):
        return self.description

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
