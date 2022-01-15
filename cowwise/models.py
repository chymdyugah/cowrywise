from django.db import models
import uuid

# Create your models here.


class MyUuid(models.Model):
    val = models.UUIDField(default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.val