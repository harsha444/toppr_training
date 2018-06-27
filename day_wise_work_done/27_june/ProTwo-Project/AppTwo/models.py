from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.first_name
