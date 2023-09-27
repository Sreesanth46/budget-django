from django.urls import path

from BudgetApp.apps.core.views import test_view

urlpatterns = [
    path("", test_view, name="test"),
]
