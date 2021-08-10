# Generated by Django 3.2.5 on 2021-08-05 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0010_alter_testsubject_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsubject',
            name='userId',
            field=models.CharField(default='2667da94f5e311ebbbbc2c4d5464fb8b', max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='SingleLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=50)),
                ('smile', models.IntegerField()),
                ('innerBrowRaise', models.IntegerField()),
                ('browRaise', models.IntegerField()),
                ('browFurrow', models.IntegerField()),
                ('noseWrinkle', models.IntegerField()),
                ('upperLipRaise', models.IntegerField()),
                ('lipCornerDepressor', models.IntegerField()),
                ('chinRaise', models.IntegerField()),
                ('lipPucker', models.IntegerField()),
                ('lipPress', models.IntegerField()),
                ('lipSuck', models.IntegerField()),
                ('mouthOpen', models.IntegerField()),
                ('smirk', models.IntegerField()),
                ('smeyeClosureile', models.IntegerField()),
                ('attention', models.IntegerField()),
                ('lidTighten', models.IntegerField()),
                ('jawDrop', models.IntegerField()),
                ('dimpler', models.IntegerField()),
                ('eyeWiden', models.IntegerField()),
                ('cheekRaise', models.IntegerField()),
                ('lipStretch', models.IntegerField()),
                ('testSubject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.testsubject')),
            ],
        ),
    ]
