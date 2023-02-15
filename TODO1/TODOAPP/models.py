from django.db import models

# Create your models here.
class Study(models.Model):
    Topic=models.CharField(max_length=250)
    Imp_level_of_topic=models.CharField(max_length=250)
    No_of_revision=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.Topic
