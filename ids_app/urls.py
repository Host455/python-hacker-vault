from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('ids/', views.ids, name='ids'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('image_results/<str:image_id>/', views.image_results, name='image_results'),
    path('log_analysis/', views.process_log_upload, name='log_analysis'),
]
