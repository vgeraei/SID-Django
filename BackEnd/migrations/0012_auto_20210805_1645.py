# Generated by Django 3.2.5 on 2021-08-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0011_auto_20210805_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singlelog',
            old_name='smeyeClosureile',
            new_name='eyeClosureile',
        ),
        migrations.AlterField(
            model_name='testsubject',
            name='userId',
            field=models.CharField(default='d2e7560af5e611eba88a2c4d5464fb8b', max_length=255, unique=True),
        ),
    ]
