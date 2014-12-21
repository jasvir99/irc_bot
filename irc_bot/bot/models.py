from django.db import models

# Create your models here.

class main(models.Model):
    channel = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    time = models.DateTimeField()
    message = models.TextField(null=True)
    type = models.CharField(max_length=20, null=True)
    hidden = models.CharField(max_length=2)

    def __unicode__(self):
            return self.name
