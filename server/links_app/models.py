import uuid
from django.db import models
 
 
class Link(models.Model):
    """
    A labeled link/resource that can be displayed to users on the homepage.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=255)
    url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = 'links'
        ordering = ['-created_at']
 
    def __str__(self):
        return self.label