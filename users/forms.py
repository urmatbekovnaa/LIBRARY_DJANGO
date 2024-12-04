from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

QUALIFICATION_CHOICES = [
    ("Junior", "Junior"),
    ("Middle", "Middle"),
    ("Senior", "Senior"),
]


class ITRegistrationForm(UserCreationForm):
    level = forms.ChoiceField(choices=QUALIFICATION_CHOICES, required=True)

    class Meta:
        model = models.ITSpecialist
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "level",
        )

    def save(self, commit=True):
        user = super(ITRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data.get("email")
        user.username = self.cleaned_data.get("username")
        user.level = self.cleaned_data.get("level")
        if commit:
            user.save()
        return user
