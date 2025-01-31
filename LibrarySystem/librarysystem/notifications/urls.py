from django.urls import path
from . import views


urlpatterns = [
    
    # path('notify-when-available/', views.notify_when_available, name='notify_when_available'),
    path('send-borrow-confirmation/', views.send_borrow_confirmation, name='send_borrow_confirmation'),
    path('notify-when-available/<int:book_id>', views.notify_when_available, name='notify_when_available'),
   
]
