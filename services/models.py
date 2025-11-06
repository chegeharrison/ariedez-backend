from django.db import models

# Create your models here.
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    detailed_description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, help_text="FontAwesome or custom icon class")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

