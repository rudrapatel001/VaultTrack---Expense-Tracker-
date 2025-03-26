from django.urls import path
from tracker.views import *


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('add/', add_expense, name='add_expense'),
    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('monthly/', monthly, name='monthly'),
    path('', landing_page, name='landing'),
]