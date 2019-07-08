from django.db import models

# Create your models here.
class TUser(models.Model):
    username = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    class Meta:
        db_table = 't_user'