from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
import polls

class RR_User(models.Model):
    rr_id = models.IntegerField(unique=True)
    user_hash=models.CharField(max_length=256,unique=True)
    # Include required fields for a custom user model

    # Count the total number of answers for the user
    def total_answers(self, mode=None):
        if mode is not None:
            return polls.models.Answer.objects.filter(author=self, status_code=mode).count()
        else:
            return polls.models.Answer.objects.filter(author=self).count()

    def __str__(self):
        return str(self.rr_id)