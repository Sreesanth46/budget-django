from BudgetApp.apps.core.models.base_model import BaseModel
from django.db import models

class UserModel(BaseModel):
    email    = models.CharField(max_length = 100, null = False, blank = False, unique = True)
    password = models.CharField(max_length = 100, null = False, blank = False)
    name     = models.CharField(max_length = 100)
    upi      = models.CharField(max_length = 100)
    phone    = models.CharField(max_length = 30)
    
    class Meta:
        db_table            = "user_master"
        managed             = True
        verbose_name        = "User Table"
        verbose_name_plural = verbose_name
        app_label           = "core"