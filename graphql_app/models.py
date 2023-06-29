from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250)
    followers = models.ManyToManyField("graphql_app.User")

class Post(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey("graphql_app.User", on_delete=models.DO_NOTHING)
