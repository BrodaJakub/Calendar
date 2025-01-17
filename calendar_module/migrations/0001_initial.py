# Generated by Django 5.1.4 on 2025-01-10 18:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tytuł')),
                ('description', models.TextField(blank=True, verbose_name='Opis')),
                ('start_time', models.DateTimeField(verbose_name='Czas rozpoczęcia')),
                ('end_time', models.DateTimeField(verbose_name='Czas zakończenia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
        ),
    ]
