from BudgetApp.apps.core.models import GroupModel, UserModel, BaseModel
from django.db import models

class GroupMemberModel(BaseModel):
    nick_name     = models.CharField(max_length = 100, blank=True)
    user_id = models.ForeignKey(
        UserModel,
        on_delete = models.CASCADE,
        db_column = "user_id",
    )
    group_id = models.ForeignKey(
        GroupModel,
        on_delete = models.CASCADE,
        db_column = "group_id",
    )
    
    class Meta:
        db_table            = "group_member"
        managed             = True
        verbose_name        = "Group Member Table"
        verbose_name_plural = verbose_name
        app_label           = "core"