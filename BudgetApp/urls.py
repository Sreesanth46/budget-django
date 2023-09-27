from django.contrib import admin
from django.urls import path, include, re_path

from BudgetApp.settings import base as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BudgetApp.apps.core.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]