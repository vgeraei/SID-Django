from django.db import models
import uuid


def get_uuid():
    return uuid.uuid1().hex

# Create your models here.
class TestSubject(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    gender = models.CharField(choices=GENDERS, max_length=50)
    age = models.IntegerField()

    EDUCATIONS = (
        ('highSchool', 'HighSchool'),
        ('bachelor', 'Bachelor'),
        ('phd', 'PhD'),
        ('master', 'Master')
    )

    education = models.CharField(choices=EDUCATIONS, max_length=50)
    occupation = models.CharField(max_length=50)
    userId = models.CharField(max_length=255, unique=True, default=get_uuid)

    def get_user_id(self):
        return self.userId


class SleepLevelLog(models.Model):
    timestamp = models.CharField(max_length=50)
    sleepLevel = models.IntegerField()
    testSubject = models.ForeignKey(TestSubject, on_delete=models.CASCADE)


class SingleLog(models.Model):
    timestamp = models.CharField(max_length=50)
    testSubject = models.ForeignKey(TestSubject, on_delete=models.CASCADE)

    # Emotions
    smile = models.IntegerField()
    innerBrowRaise = models.IntegerField()
    browRaise = models.IntegerField()
    browFurrow = models.IntegerField()
    noseWrinkle = models.IntegerField()
    upperLipRaise = models.IntegerField()
    lipCornerDepressor = models.IntegerField()
    chinRaise = models.IntegerField()
    lipPucker = models.IntegerField()
    lipPress = models.IntegerField()
    lipSuck = models.IntegerField()
    mouthOpen = models.IntegerField()
    smirk = models.IntegerField()
    eyeClosure = models.IntegerField()
    attention = models.IntegerField()
    lidTighten = models.IntegerField()
    jawDrop = models.IntegerField()
    dimpler = models.IntegerField()
    eyeWiden = models.IntegerField()
    cheekRaise = models.IntegerField()
    lipStretch = models.IntegerField()
