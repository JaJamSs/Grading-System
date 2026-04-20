from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Redirects to dashboard
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard_test/', views.dashboard_test_view, name='dashboard_test'),
    path('grading/', include('grading_system.urls')),
]