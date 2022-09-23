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
        verbose_name='Артикль',
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

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_products'