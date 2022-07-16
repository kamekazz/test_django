import uuid
from django.db import models

from users.models import Profile

# Create your models here.


class Attack(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    telephone = models.ManyToManyField('TelephoneNumber', blank=True)
    text_message = models.TextField(max_length=200, default='hi',)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.title


class TelephoneNumber(models.Model):
    name = models.CharField(max_length=200)
    target_number = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True,
        primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.name
