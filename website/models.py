from django.db import models
from django.contrib.auth.models import User

def get_document_dir(instance, filename):
    return '%s/attachment/%s' % (instance.user, filename)

class Proposal(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    objective = models.CharField(max_length=512)
    abstract = models.TextField(max_length=700)
    bio = models.TextField(max_length=500)
    link = models.CharField(max_length=128)
    attachment = models.FileField(upload_to=get_document_dir)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
