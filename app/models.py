from django.db import models
import uuid


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lastName = models.CharField(max_length=150)
    firstName = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    createAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-createAt"]

    def __str__(self):
        return f"{self.firstName} {self.lastName}"