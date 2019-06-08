from django.contrib.auth import get_user_model
from django.db import models


class GroupModel(models.Model):
    user = models.ManyToManyField(get_user_model())
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
