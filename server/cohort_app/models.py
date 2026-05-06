import uuid
from django.db import models


class Cohort(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    invite_code = models.TextField(unique=True)

    class Meta:
        db_table = 'cohorts'


class ValidEmail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    email = models.EmailField()
    
    class Meta:
        db_table = 'valid_emails'
        unique_together = [('cohort', 'email')]


class ResourceLink(models.Model):
    url = models.TextField(primary_key=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    label = models.TextField()

    class Meta:
        db_table = 'resource_links'

class DailyLink(models.Model):
    url = models.TextField(primary_key=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    label = models.TextField()

    class Meta:
        db_table = 'daily_links'
