from django.db import models

class Users(models.Model):
  first_name = models.CharField(max_length = 255)
  last_name = models.CharField(max_length = 255)
  email_address = models.CharField(max_length = 255)
  age = models.IntegerField()
  create_at = models.DateTimeField(auto_now_add = True)
  update_at = models.DateTimeField(auto_now = True)
