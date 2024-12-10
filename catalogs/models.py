from django.db import models
from django.conf import settings
import uuid

class Catalog(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="catalogs")

    def __str__(self):
        return self.name
    

class Category(models.Model):
    id = models.UUIDField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    catalog = models.ForeignKey(Catalog, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name