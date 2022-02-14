from django.db import models

# Create your models here.
class UserRegistry(models.Model):
    class Meta:
        app_label = 'usermanager'
        db_table = 'user_registry'
    
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    