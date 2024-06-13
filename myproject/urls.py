# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include URLs from myapp
    path('accounts/', include('django.contrib.auth.urls')),  # Include default auth URLs
]
