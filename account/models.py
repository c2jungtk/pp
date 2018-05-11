from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.urls import reverse
# Create your models here.

class Member(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('product:product_detail', kwargs={'pk': self.pk})