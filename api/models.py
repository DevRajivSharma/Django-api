from django.db import models

# Create your models here.
class Name(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)

    def __str__(this):
        return f"{this.f_name} {this.l_name}"
    