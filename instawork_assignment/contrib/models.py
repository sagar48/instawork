import uuid
from django.db import models


class BaseModel(models.Model):
    '''
        Single common class with uuid as pk and created & updates timestamps
    '''

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
