# Generated by Django 4.2.5 on 2023-09-24 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('duration_seconds', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ViewRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched_duration', models.IntegerField(default=0)),
                ('is_watched', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySystem.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySystem.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('lessons', models.ManyToManyField(to='StudySystem.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='AccesToProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acces', models.BooleanField(default=False)),
                ('Products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySystem.product')),
            ],
        ),
    ]
