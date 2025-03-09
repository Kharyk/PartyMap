from django.db import models
from partymap.group import Group

class Artist(models.Model):
    name = models.CharField(max_length=100)
    type_of = models.CharField(max_length=60)
    since = models.TimeField(auto_now_add=True)
    group = models.ManyToManyField(Group)
    language = models.CharField(max_length=50)
    info = models.TextField()
    image = models.ImageField(upload_to='artist/', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.name

# Remove the redundant import of Group
