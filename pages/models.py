from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    agree = models.BooleanField()

    def __str__(self):
        return f"{self.name} {self.surname}"
