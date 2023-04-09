from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from polls.models import Answer


# Create your models here.
class RR_User(AbstractBaseUser):
    user_id=None
    user_name=None
    rr_id=None

class RR_User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, unique=True)
    rr_id = models.IntegerField(unique=True)

    # Include required fields for a custom user model
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    # Count the total number of answers for the user
    def total_answers(self):
        return Answer.objects.filter(author=self).count()

    def __str__(self):
        return self.user_name