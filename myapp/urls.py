
from atexit import register
from django.urls import path
from myapp import views

 


urlpatterns = [
    path('home', views.home, name='home'),

    path('dashboard/', views.deshboard, name='dashboard'),
    path('blogs/', views.blogs, name='blogs'),
    path('about/', views.about, name='about'),
    path('production/', views.production, name='production'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('add', views.add, name='add'),   
    path('register/', views.register, name='register'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('hotel-upload/', views.hotel_image_view, name='hotel_upload'),
    path('success/', views.success, name='success'),
    path('company-entry/', views.company_entry, name='company_entry'),
    path('employee-info/', views.employee_info1, name='employee_info'),
    path('Budget/', views.budget_entry, name='budget_entry'),
    path('budget_info/', views.budget_info, name='budget_info'),
    path('search_budget/', views.search_budget, name='search_budget'),
    path('budget/<int:pk>/edit/', views.budget_edit, name='budget_edit'),
    path('budget/<int:pk>/delete/', views.budget_delete, name='budget_delete'),

]
