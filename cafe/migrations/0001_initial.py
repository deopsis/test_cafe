# Generated by Django 3.2.5 on 2021-07-13 12:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(upload_to='cafe/', verbose_name='Изображение')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('description', models.TextField(verbose_name='Описание')),
                ('year', models.DateField(default=datetime.date.today, verbose_name='Дата регистрации')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default='False', verbose_name='Черновик')),
            ],
            options={
                'verbose_name': 'Кафе',
                'verbose_name_plural': 'Кафе',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст отзыва')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.cafe', verbose_name='Кафе')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='cafe.cafe', verbose_name='Кафе')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cafe_shots/', models.ImageField(upload_to='', verbose_name='Фото интерьера')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.cafe', verbose_name='Кафе')),
            ],
            options={
                'verbose_name': 'Фотография интерьера',
                'verbose_name_plural': 'Фотографии интерьера',
            },
        ),
        migrations.AddField(
            model_name='cafe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.category', verbose_name='Категория'),
        ),
    ]