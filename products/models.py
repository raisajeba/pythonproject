from django.db import models
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=10.0)

    def __str__(self):
        return self.title


# Create your models here.
