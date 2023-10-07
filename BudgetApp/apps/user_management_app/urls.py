from django.urls import path
from BudgetApp.apps.user_management_app.views import register_user, verify_email, sign_up, login, verify_access_token

urlpatterns = [
    path("register", register_user, name="register"),
    path("verify-email", verify_email, name="verify-email"),
    path("signup", sign_up, name="sign-up"),
    path("login", login, name="login"),
    path("verify-token", verify_access_token, name="verify-access-token"),
]
