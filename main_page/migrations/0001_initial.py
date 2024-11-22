# Generated by Django 4.2.16 on 2024-11-21 14:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book/', verbose_name='Загрузите картинку')),
                ('title', models.CharField(max_length=100, verbose_name='Введите название книги')),
                ('description', models.TextField(default='Lorem Ipsum', verbose_name='Введите описание книги')),
                ('price', models.FloatField(verbose_name='Введите цену книги')),
                ('published_data', models.DateField(verbose_name='Дата публикации')),
                ('genre', models.CharField(choices=[('Фантастика', 'Фантастика'), ('Детектив', 'Детектив'), ('Роман', 'Роман'), ('Приключения', 'Приключения')], max_length=100, verbose_name='Жанр книги')),
                ('mail', models.EmailField(max_length=254, verbose_name='Введите почту автора')),
                ('author', models.CharField(max_length=100, verbose_name='Введите автора книги')),
                ('audio_book', models.URLField(verbose_name='Введите ссылку на аудиокнигу')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('description', models.TextField(verbose_name='Оставьте отзыв о книге')),
                ('mark', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Укажите оценку от 1 до 5')),
                ('review_books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_books', to='main_page.books')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]