from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(null=True, blank=True)
    social_links = models.TextField(null=True, blank=True)

    def set_links(self, x):
        self.social_links = ";".join(x)

    def get_links(self):
        return self.social_links.split(';')
