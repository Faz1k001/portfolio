from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=120, help_text="Masalan: Python Django Developer")
    about = models.TextField()
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    telegram = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.full_name


class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=80)
    level = models.PositiveIntegerField(default=70, help_text="0-100")

    def __str__(self):
        return self.name