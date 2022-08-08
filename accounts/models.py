from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    dob = models.DateField(null=True,blank=True)
    student = models.BooleanField(default=True)

class Student(models.Model):
    user = models.ForeignKey("accounts.User",related_name="Students",on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)