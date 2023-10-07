from typing import Any
import bcrypt
from BudgetApp.apps.core.models.base_model import BaseModel
from django.db import models


class UserModelManager(models.Manager):
    def create_user(self, **kwargs: Any) -> Any:
        password = kwargs.pop('password', None)
        
        if password is None:
            raise ValueError("Password is required when creating a user.")
        
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user = self.create(**kwargs, password=password_hash)
        return user


class UserModel(BaseModel):
    email    = models.CharField(max_length = 100, null = False, blank = False, unique = True)
    password = models.CharField(max_length = 100, null = False, blank = False)
    name     = models.CharField(max_length = 100)
    upi      = models.CharField(max_length = 100)
    phone    = models.CharField(max_length = 30)
    
    objects = UserModelManager()

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    class Meta:
        db_table            = "user_master"
        managed             = True
        verbose_name        = "User Table"
        verbose_name_plural = verbose_name
        app_label           = "core"