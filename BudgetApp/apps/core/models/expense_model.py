from BudgetApp.apps.core.models import UserModel, BaseModel
from django.db import models

class ExpenseModel(BaseModel):
    name        = models.CharField(max_length = 100, null = False, blank = False)
    description = models.CharField(max_length = 100, blank = True)
    amount      = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    user_id     = models.ForeignKey(
        UserModel,
        on_delete = models.CASCADE,
        db_column = "user_id",
    )
    
    class Meta:
        db_table            = "expense_master"
        managed             = True
        verbose_name        = "Expense Table"
        verbose_name_plural = verbose_name
        app_label           = "core"