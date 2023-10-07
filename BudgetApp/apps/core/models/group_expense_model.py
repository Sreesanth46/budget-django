from BudgetApp.apps.core.models import GroupMemberModel, BaseModel, ExpenseModel
from django.db import models

class GroupExpenseModel(BaseModel):
    description = models.CharField(max_length = 100, blank = True)
    expense_id  = models.ForeignKey(
        ExpenseModel,
        on_delete = models.CASCADE,
        db_column = "expense_id",
    )
    created_by  = models.ForeignKey(
        GroupMemberModel,
        on_delete = models.CASCADE,
        db_column = "created_by",
    )
    
    class Meta:
        db_table            = "group_expense"
        managed             = True
        verbose_name        = "Group Expense Table"
        verbose_name_plural = verbose_name
        app_label           = "core"