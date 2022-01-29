from django.db import models

class BaseModel(models.Model):
    """ Base model for other apps """
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    modified_date = models.DateField(auto_now=True, auto_now_add=False)
    deleted_date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = "Base Model"
        verbose_name_plural = 'Base Models'

