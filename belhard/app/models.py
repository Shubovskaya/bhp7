from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='название',
        help_text='Макс. 24 символа'
    )
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name='род. категория'
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='Макс. 24 символа'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('is_published', 'name')


class Product(models.Model):
    title = models.CharField(
        max_length=36,
        verbose_name='название',
        help_text='Макс. 36 символов'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='Описание',
        help_text='Макс. 16 символов'
    )
    article = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='Артикул',
        help_text='Макс. 16 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text='Макс. 999999.99'
    )
    count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='количество'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория'
    )
    image = models.ImageField(
        upload_to='products',
        verbose_name='картинка',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')


class Order(models.Model):
    title = models.CharField(
        max_length=45,
        verbose_name='заказ',
        help_text='Макс. 36 символов'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )
    date_created = models.DateTimeField(
        default=datetime.now(),
        blank=True
    )
    is_paid = models.BooleanField(
        default=0,
        verbose_name='статус оплаты',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_orders'
        verbose_name = 'заявка/заказ'
        verbose_name_plural = 'заявки/заказы'
        ordering = ('product', 'title', 'user')


class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    message = models.CharField(max_length=1024)
    date_created = models.DateTimeField(default=datetime.utcnow(), verbose_name='дата публикации')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'app_contacts'
        ordering = ('date_created', )
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'