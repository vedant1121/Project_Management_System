from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    contactno = models.CharField(max_length=12)
    message = models.CharField(max_length=200)


    class Meta:
        db_table = 'contactus'

    def __str__(self):
        return self.name