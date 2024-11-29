from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название особенности")

    def __str__(self):
        return self.name


class Device(models.Model):
    image = models.ImageField(upload_to='devices/', verbose_name="Загрузите картинку")
    name = models.CharField(max_length=150, verbose_name="Название устройства")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель устройства")
    price = models.FloatField(verbose_name="Цена устройства")
    release_date = models.DateField(verbose_name='Дата выпуска')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='devices', null=True)
    features = models.ManyToManyField(Feature, related_name='devices')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Review_device(models.Model):
    review_devices = models.ForeignKey(Device, on_delete=models.CASCADE,
                                     related_name='review_devices')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзыв')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_devices} - {self.created_at}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
