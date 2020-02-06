from django.db import models

class Coach(model.Models):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    M = 'Male'
    F = 'Female'
    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female'),
    )
    gender = models.Charfield(choices=GENDER_CHOICES, default=None)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)
    skype = models.CharField(max_length=25)
    discription = models.TextField(max_length=250)

    def __str__(self):
        return self.name