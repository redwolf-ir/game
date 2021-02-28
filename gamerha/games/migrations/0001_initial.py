# Generated by Django 3.0.8 on 2020-07-13 06:19

from django.db import migrations, models
import django.db.models.deletion
import games.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEVELOPER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('logo', models.FileField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GENRE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PLATFORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('logo', models.FileField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PUBLISHER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('logo', models.FileField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GAME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('box_art', models.FileField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('Age_rating', models.CharField(choices=[('EVERYONE', 'همه کس'), ('EVERYONE10PLUS', 'همه کس +10'), ('TEEN', 'نوجوان'), ('MATURE17PLUS', 'بالغ +17'), ('ADULTSONLY', 'بزرگ سالان'), ('RATINGPENDING', 'در انتظار')], default=[('EVERYONE', 'همه کس'), ('EVERYONE10PLUS', 'همه کس +10'), ('TEEN', 'نوجوان'), ('MATURE17PLUS', 'بالغ +17'), ('ADULTSONLY', 'بزرگ سالان'), ('RATINGPENDING', 'در انتظار')], max_length=45)),
                ('developer', models.ManyToManyField(to='games.DEVELOPER')),
                ('genre', models.ManyToManyField(to='games.GENRE')),
                ('platforms', models.ManyToManyField(to='games.PLATFORM')),
                ('publisher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='games.PUBLISHER')),
            ],
        ),
    ]
