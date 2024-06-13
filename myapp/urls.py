# myapp/urls.py

from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),  # Add this line
]
