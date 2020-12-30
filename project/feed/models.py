from django.db import models
from  django.conf import settings
from api.models import UserProfile
from workspace.models import Board

# Create your models here.


class Feed(models.Model):
      user_profile= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
      title=models.CharField(max_length=255)
      text=models.TextField(blank=True)
      workspace=models.ForeignKey(Board,on_delete=models.CASCADE)
      created_on=models.DateTimeField(auto_now_add=True,auto_now=False)

      def __str__(self):
          return self.title


class Cards(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255,blank=True)
    feed=models.ForeignKey(Feed,on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



