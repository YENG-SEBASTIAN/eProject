
#app urls

from django.urls import path

from . import views 

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('account/register/', views.register_view, name='register'),
    path('', views.dashboard_view, name='dashboard'),
]