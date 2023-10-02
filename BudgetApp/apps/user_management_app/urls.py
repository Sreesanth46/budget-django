from django.urls import path
from BudgetApp.apps.user_management_app.views import register_user, verify_email, sign_up

urlpatterns = [
    path("register", register_user, name="register"),
    path("verify-email", verify_email, name="verify-email"),
    path("signup", sign_up, name="sign-up"),
]
