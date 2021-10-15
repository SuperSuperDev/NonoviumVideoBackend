import random

from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def random_string():
    return str(random.randint(10000, 99999))


class User(AbstractUser):
    """Default user for Nonovium Video Backend."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    user_image = CharField(
        max_length=250,
        default=f"https://avatars.dicebear.com/api/avataaars/{random_string()}.svg?size=150",
    )
    """User profile image If user does not supply an image, we create a random one"""

    bio = TextField(
        max_length=500, blank=True, default="This user has not added a bio yet"
    )
    dark_mode = BooleanField(default=False)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
