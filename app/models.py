from django.db import models
import uuid



class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lastName = models.CharField(max_length=150)
    firstName = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)
    createAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-createAt"]

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class Patient(Person):
    pass
    
class Medecin(Person):
    expertise = models.CharField(max_length=150)
    
class Profile(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete = models.CASCADE,
        related_name = "profile"
    )
    photo = models.ImageField(upload_to="profiles/photos")
    biography = models.TextField()
     
    def __str__(self):
        return f"Profile of {self.person.firstName} {self.person.lastName}"

    

    