from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Snacks(models.Model):

    title_field = models.CharField(max_length=256)
    purchaser_field = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description_field=models.TextField(blank=True)


    def __str__(self):
        return self.title_field

    def get_absolute_url(self):
        return reverse("snacks_detail", args=[str(self.id)])    
