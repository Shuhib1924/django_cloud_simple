from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


def profile_path(instance, filename):
    date_path = datetime.now().strftime("%Y/%m/%d")
    return f"profile/{instance.user.username}/{date_path}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=profile_path, blank=True)

    def __str__(self):
        return self.user.username
