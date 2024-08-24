from django.db import models
from .managers import CustomClassManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomClassManager()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=250)
    bio = models.CharField(max_length=1500)
    description = models.CharField(max_length=5000)
    profile = models.ImageField(upload_to="user_profile")

    def __str__(self):
        return f"{self.fullname}"


class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    institute = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    course = models.CharField(max_length=600)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    image = models.ImageField(upload_to="educations")

    def __str__(self):
        return f"{self.institute} - {self.course}"


class Certification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    domain = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    center_name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    image = models.ImageField(upload_to="certificates")

    def __str__(self):
        return f"{self.domain} - {self.category}"


class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    domain = models.CharField(max_length=250)
    period = models.CharField(max_length=250)
    image = models.ImageField(upload_to="experiences")

    def __str__(self):
        return f"{self.company_name} - {self.domain}"


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.CharField(max_length=7000)
    link = models.CharField(max_length=500)
    image = models.ImageField(upload_to="projects")

    def __str__(self):
        return f"{self.project_name}"
