import uuid
from django.db import models
from cohort_app.models import Cohort


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cohort = models.ForeignKey(Cohort, on_delete=models.SET_NULL, null=True)
    name = models.TextField()
    email = models.EmailField(null=False, unique=True)
    google_id = models.TextField(unique=True)

    class Meta:
        db_table = 'students'


class Instructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    email = models.EmailField(null=False, unique=True)
    api_key = models.TextField(null=False, unique=True)

    class Meta:
        db_table = 'instructors'

