from django.urls import path
from .import views

urlpatterns = [
    
    path('add_schedule/', views.add_duty_schedule, name='add_duty_schedule'),
    path('display_schedule/', views.display_duty_schedule, name='display_duty_schedule'),
    path('update_schedule/<int:pk>/', views.update_schedule, name='update_schedule'),
    path('savedata/<int:pk>/',views.savedata,name='savedata'),
    
]
