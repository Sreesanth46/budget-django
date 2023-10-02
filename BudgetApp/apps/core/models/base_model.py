from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False, db_column='id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True