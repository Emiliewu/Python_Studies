from django.db import models

class CourseManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    name = postData["name"]
    if not name or name.isspace():
      errors["name"] = "Please input the course name!"
    elif len(name) <= 5:
      errors["name"] = "Course name should be longer than 5 charactors!"
    return errors

class Course(models.Model):
  name = models.CharField(max_length=255)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  objects = CourseManager()

class DescriptionManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    description = postData["desc"]
    if not description or description.isspace():
      errors["desc"] = "Please write the description!"
    elif len(description) <= 15:
      errors["desc"] = "The description shoud be longer than 15 charactors!"
    return errors

class Description(models.Model):
  course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
  desc = models.TextField(null=True)
  create_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  objects = DescriptionManager()

class CommentManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    comment = postData["comment"]
    if not comment or comment.isspace():
      errors["comment"] = "Please write some comments!"
    elif len(comment) <= 10:
      errors["comment"] = "The comment should be longer than 10 charactors!"
    return errors

class Comment(models.Model):
  comment = models.TextField(null=True)
  course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
  create_at = models.DateTimeField(auto_now_add=True, null=True)
  update_at = models.DateTimeField(auto_now=True, null=True)
  objects = CommentManager()


