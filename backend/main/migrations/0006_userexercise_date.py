# Generated by Django 3.2.23 on 2023-11-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_exerciseamount_userexercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='userexercise',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]