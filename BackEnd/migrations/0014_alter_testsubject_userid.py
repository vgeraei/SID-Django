# Generated by Django 3.2.5 on 2021-08-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0013_auto_20210805_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsubject',
            name='userId',
            field=models.CharField(default='977d6a0ef6b711eb91b52c4d5464fb8b', max_length=255, unique=True),
        ),
    ]