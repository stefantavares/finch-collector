from django.db import models
from django.urls import reverse

# Create your models here.


class Finch(models.Model):
    type = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.id}) - {self.type}'

    def get_absolute_url(self):
        return reverse('finches_detail', kwargs={'finch_id': self.id})
