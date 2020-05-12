from django.db import models
from  django.conf import settings

# Create your models here.


class Feed(models.Model):
      user_profile= models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE

      )

      text=models.CharField(max_length=255)
      created_on=models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.text