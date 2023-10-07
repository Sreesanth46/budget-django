from BudgetApp.apps.core.models import BaseModel, GroupExpenseModel
from django.db import models

class SplitExpenseModel(BaseModel):
    split_amount      = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    group_expense_id  = models.ForeignKey(
        GroupExpenseModel,
        on_delete = models.CASCADE,
        db_column = "group_expense_id",
    )
    
    class Meta:
        db_table            = "split_expense"
        managed             = True
        verbose_name        = "Split Expense Table"
        verbose_name_plural = verbose_name
        app_label           = "core"