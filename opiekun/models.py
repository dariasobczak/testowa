from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Grupa(models.Model):
    nazwa = models.CharField(max_length=25)
    rocznik = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "grupy"

    def __str__(self):
        return self.nazwa


class Opiekun(models.Model):
    user = models.OneToOneField(User)
    grupy = models.ManyToManyField(Grupa)
    
    class Meta:
        verbose_name_plural = "opiekunowie"

    def __str__(self):
        return "{imie} {nazwisko}".format(imie=self.user.first_name, nazwisko=self.user.last_name)
