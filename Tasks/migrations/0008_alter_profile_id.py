# Generated by Django 4.2 on 2023-07-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0007_alter_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
