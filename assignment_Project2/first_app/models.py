from django.db import models

# Create your models here.
class taskFormModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    status = models.BooleanField(default= False)