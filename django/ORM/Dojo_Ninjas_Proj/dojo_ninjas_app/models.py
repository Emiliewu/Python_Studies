from django.db import models

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  desc = models.CharField(max_length=255, default="old dojo")

  def __str__(self):
    return f'Dojo({name})'

class Ninja(models.Model):
  dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)

  def __str__(self):
    return f'Ninja({first_name} {last_name})'

