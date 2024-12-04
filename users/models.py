from django.db import models
from django.contrib.auth.models import User


class ITSpecialist(User):
    QUALIFICATION_CHOICES = [
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
    ]
    salary = models.PositiveIntegerField(default=500)
    choice = models.CharField(
        max_length=10, choices=QUALIFICATION_CHOICES, default="Junior"
    )
    level = models.CharField(max_length=50, default="не определено")

    def save(self, *args, **kwargs):
        if self.level == "Junior":
            self.salary = 300
        elif self.level == "Middle":
            self.salary = 1000
        elif self.level == "Senior":
            self.salary = 2000
        else:
            self.salary = 0

        super().save(*args, **kwargs)
