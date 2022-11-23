from django.db import models
class generalFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modefied_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    