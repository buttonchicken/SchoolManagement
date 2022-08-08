from django.db import models
from accounts.models import User
import jsonfield
import uuid
# Create your models here.

class Class(models.Model):
    class_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    class_teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    subjectlist = models.CharField(max_length=100)
    students = jsonfield.JSONField(default={})
    class Meta:
        verbose_name_plural = "Class"
