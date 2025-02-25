from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .handler import create_profile

post_save.connect(receiver=create_profile, sender=User)
