from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    if Show.objects.filter(title__iexact=postData["title"]):
      errors["title"] = "The TV show title already exists!"    
    if len(postData["title"]) < 2:
      errors["title"] = "Show title should be at least 2 charactors!"
    if len(postData["network"]) < 3:
      errors["network"] = "Show network should be at least 3 charactors!"
    if len(postData["description"]) > 0 and len(postData["description"]) < 10:
      errors["description"] = "Show description should be at least 10 charactors or leave it empty!"
    if datetime.strptime(postData["release_date"], "%Y-%m-%d") >= datetime.now():
      errors["release_date"] = "Show release date should be prior to today!"
    return errors

  
class Show(models.Model):
  title = models.CharField(max_length=255)
  network = models.CharField(max_length=50)
  release_date = models.DateField(auto_now=False,auto_now_add=False,null=True)
  description = models.TextField(null=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()
