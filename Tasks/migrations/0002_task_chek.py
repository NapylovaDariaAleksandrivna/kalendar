# Generated by Django 4.2 on 2023-07-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='chek',
            field=models.BooleanField(default=False),
        ),
    ]
