from django.db import models
from django.contrib.auth.models import User
from books.models import Books

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ": " + str(self.book)

class Notification(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    seller = models.CharField(max_length=10)

    def __str__(self):
        return self.user + ": " + str(self.book)