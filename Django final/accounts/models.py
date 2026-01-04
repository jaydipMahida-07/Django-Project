from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields here if needed (e.g., is_author, bio, etc.)
    # For now, we'll stick to the basics, but it's good practice to start with a custom user model.
    pass

    def __str__(self):
        return self.username
