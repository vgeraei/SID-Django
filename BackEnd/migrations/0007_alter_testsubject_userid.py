# Generated by Django 3.2.5 on 2021-07-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0006_alter_testsubject_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsubject',
            name='userId',
            field=models.CharField(default='50499410edea11eb9b2a2c4d5464fb8b', max_length=255, unique=True),
        ),
    ]
