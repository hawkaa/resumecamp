from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    
    owner = models.ForeignKey(User)

    name = models.CharField(max_length=255)
    address = models.TextField(null=True)
    email = models.EmailField(null=True)
    born = models.DateField(null=True)

    def __unicode__(self):
        return self.name
