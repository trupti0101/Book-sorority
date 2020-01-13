from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    image = models.FileField(upload_to='', null=True, verbose_name="")
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    isbn = models.IntegerField()
    edition = models.IntegerField()
    publisher = models.CharField(max_length=100)
    publishyear = models.IntegerField()
    sold = models.BooleanField()

    def __str__(self):
        return self.name + ": " + str(self.image)