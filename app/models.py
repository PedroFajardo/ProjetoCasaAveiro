from django.db import models

class thing(models.Model):
    name = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    category = models.CharField(max_length = 30)
    def __str__(self):
        return self.name