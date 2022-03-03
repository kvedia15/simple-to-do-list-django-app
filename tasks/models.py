from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_string_not_empty(value):
    if len(value) > 0:
        raise ValidationError(
            _('%(value)s is an empty string'),
            params={'value': value},
        )
# Create your models here.
class Task(models.Model):
    id = models.TextField(primary_key=True)
    task = models.TextField()
    status=models.BooleanField(default=False)

