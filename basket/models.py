from django.db import models
from django.core.validators import RegexValidator
from main_page.models import Books

class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя заказчика")
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        verbose_name="Телефон заказчика"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Email заказчика")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Выбранная книга")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ от {self.name} на книгу {self.book.title}"


