from django.urls import path
from . import views

#Url Config
urlpatterns = [
    path('', views.total_interest_calculator),
    path('submit_data/', views.calculate_interest)
]