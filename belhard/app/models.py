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
    is_published = models.BooleanField(default=False, verbose_name='публикация')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('is_published', 'name')