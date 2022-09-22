from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class info(models.Model):
    text = RichTextField(blank=True, null=True)
  