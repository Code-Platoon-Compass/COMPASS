import uuid
from django.db import models


class VocabList(models.Model):
    lecture_url = models.TextField(primary_key=True)

    class Meta:
        db_table = 'vocab_lists'


class VocabItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vocab_list_url = models.ForeignKey(
        VocabList,
        on_delete=models.CASCADE,
        
        to_field='lecture_url',
    )
    term = models.TextField()
    definition = models.TextField()

    class Meta:
        db_table = 'vocab_items'
