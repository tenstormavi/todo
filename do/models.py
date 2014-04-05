from django.db import models

# Create your models here.
class do(models.Model):
    date_time_start = models.DateTimeField()
    description = models.TextField()
    date_time_end = models.DateTimeField()
    status = models.BooleanField()

    class Meta():
        verbose_name = 'do'
        verbose_name_plural = 'do'
