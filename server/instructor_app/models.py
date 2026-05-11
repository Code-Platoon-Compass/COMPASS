from django.db import models
import uuid

# Create your models here.
class Instructor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    email = models.EmailField(null=False, unique=True)
    api_key = models.TextField(null=False, unique=True)

    class Meta:
        db_table = 'instructors'