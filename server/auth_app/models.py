from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from cohort_app.models import Cohort


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cohort = models.ForeignKey(Cohort, on_delete=models.SET_NULL, null=True)
    name = models.TextField()
    email = models.EmailField(null=False, unique=True)
    google_id = models.TextField(unique=True)

    class Meta:
        db_table = 'students'
