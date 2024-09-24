from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'

    def __str__(self):
        return self.title
