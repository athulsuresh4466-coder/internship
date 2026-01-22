from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=100,
        help_text="FontAwesome icon class (e.g. fas fa-bolt)",
        blank=True
    )

    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="features"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(
        max_length=100,
        help_text="FontAwesome icon class (e.g. fas fa-industry)",
        blank=True
    )

    def __str__(self):
        return f"{self.service.title} - {self.title}"





class HomeService(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=100,
        help_text="FontAwesome icon class (e.g. fas fa-bolt)"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title






class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"










# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    rollno = models.CharField(max_length=6)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

