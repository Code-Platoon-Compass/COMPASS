import uuid
from django.db import models

class Cohort(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    label = models.TextField()

    class Meta:
        db_table = 'resource_links'
        unique_together = [('cohort', 'url')]

class DailyLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    label = models.TextField()

    class Meta:
        db_table = 'daily_links'
        unique_together = [('cohort', 'url')]
