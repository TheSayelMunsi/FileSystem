from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class UploadedFile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    # Add other fields as needed

