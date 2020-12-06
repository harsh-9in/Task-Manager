from django.db import models
from  django.conf import settings

# Create your models here.
class Board(models.Model):
    title=models.CharField(max_length=100)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
