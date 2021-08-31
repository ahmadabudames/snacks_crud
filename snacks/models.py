from django.db import models
from django.contrib.auth import get_user_model


class Snacks(models.Model):

    title_field = models.CharField(max_length=256)
    purchaser_field = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description_field=models.TextField(blank=True)
