# Generated by Django 4.2 on 2023-07-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0011_alter_task_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
