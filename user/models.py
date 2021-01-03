from django.db import models
# Create your models here.


class UserInfo(models.Model):

    # USER_CHOICES = (
    #     ('reader', 'Reader'),
    #     ('admin', 'Administrator'),
    # )
    # GENDER_CHOICES = (
    #     ('male', 'male'),
    #     ('female', 'female'),
    # )

    name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=25)
    permission = models.CharField(max_length=20, default='reader')
    gender = models.CharField(max_length=20, default='male')

    def __str__(self):
        return self.name