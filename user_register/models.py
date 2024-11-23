from django.db import models

# Create your models here.
class user_prof(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='user_image/', default='def.png', null=True, blank=True)

def __str__(self):
    return self.name    