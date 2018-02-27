from django.db import models

# Create your models here.

class District(models.Model):
    code = models.CharField(max_length=16, primary_key=True, unique=True, null=False, blank=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    parent = models.CharField(max_length=16, null=True, blank=False)
    level = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "district"
