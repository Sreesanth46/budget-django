from BudgetApp.apps.core.models import UserModel, BaseModel
from django.db import models

class GroupModel(BaseModel):
    name        = models.CharField(max_length = 100, null = False, blank = False)
    description = models.CharField(max_length = 100, blank = True)
    admin_id    = models.ForeignKey(
        UserModel,
        on_delete = models.CASCADE,
        db_column = "admin_id",
    )
    
    class Meta:
        db_table            = "group_master"
        managed             = True
        verbose_name        = "Group Table"
        verbose_name_plural = verbose_name
        app_label           = "core"