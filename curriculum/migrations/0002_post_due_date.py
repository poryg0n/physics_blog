# Generated by Django 4.2.1 on 2024-03-28 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]