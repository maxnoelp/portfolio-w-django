from django.db import models


class guestBook(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    link = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
