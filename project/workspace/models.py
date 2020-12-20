from django.db import models
from  django.conf import settings
from api.models import UserProfile

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_by=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
