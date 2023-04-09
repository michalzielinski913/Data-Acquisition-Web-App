from django.db import models

from rr_users.models import RR_User

# Create your models here.
class Answer(models.Model):
    STATUS = (
        ('NW', 'New'),
        ('AC', 'Accepted'),
        ('RJ', 'Rejected'),
    )
    text = models.TextField()
    author = models.ForeignKey(RR_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=True, null=True)
    wants_contact = models.BooleanField(default=False, blank=True)
    status_code = models.CharField(
        max_length=2,
        choices=STATUS,
        default='NW',
    )
    def __str__(self):
        return f"{self.author}: {self.text[:50]}..."